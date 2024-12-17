from fastapi import FastAPI, status, Depends, APIRouter

#utilities
from utility.common_response import response
#import success messages from utility
from utility.common_success_messages import (
   DATA_SENT_SUCCESS , DATA_INSERT_SUCCESS, DATA_UPDATE_SUCCESS, DATA_SOFT_DELETE_SUCCESS, DATA_RESTORE_SUCCESS, DATA_HARD_DELETE_SUCCESS, OTP_VERIFICATION_SUCCESS, MAIL_SENT_SUCCESS, PASSWORD_RESET_SUCCESS
)
#import error messages from utility
from utility.common_error_messages import (
   DATA_SENT_ERR , DATA_INSERT_ERR, DATA_NOT_FOUND_ERR, DATA_UPDATE_ERR, DATA_SOFT_DELETE_ERR, DATA_RESTORE_ERR, DATA_HARD_DELETE_ERR, OTP_VERIFICATION_ERR, MAIL_SENT_ERR, USER_ACTIAVTED_ERR, PASSWORD_MATCH_ERR
)

#import sql alchemy model
from .. import sql_alchemy_models
#import sql alchemy database engine
from database_handler.sql_alchemy_db_handler import db_engine, SessionLocal, db_flush
#import session from sql alchemy
from sqlalchemy.orm import Session

#import query operation functions from sql alchemy
from sqlalchemy import desc

#make url parameters optional
from typing import Optional
#usae pydantic model to define the structure of the data that is to be inserted in the api end-point
from pydantic_custom_models.Users import CreateUpdateUserModel, BlockUnblockUsersModel, SoftDeleteRestoreUserModel, VerifyOTPUsersModel, ResendOtp, RequestResetPasswordModel, ResetPasswordModel

#import a utility that hashes user password
from utility.hash_password import hash_pass_fun, hash_reset_pass_fun

#Email related imports
from utility.send_mail import send_email_async, send_email_background
from fastapi import BackgroundTasks
from random import randint

router = APIRouter(
    prefix="/users"
)

sql_alchemy_models.Base.metadata.create_all(bind=db_engine)

#Create a user in a database table
@router.post('/register')
def create_users(userModel : CreateUpdateUserModel, background_tasks : BackgroundTasks, db : Session = Depends(db_flush)):
    try:
       # before we create the user we need to create the hash of the password
       #hash the use password
       hashed_pass_user_model = hash_pass_fun(userModel)
       #Now that the password is hashed we can create a new user
       new_user = sql_alchemy_models.UserMaster(**hashed_pass_user_model.model_dump())
       db.add(new_user)
       db.commit()
       db.refresh(new_user)
       if not new_user:
           return response(status=status.HTTP_400_BAD_REQUEST,error=DATA_INSERT_ERR)

       # Generate otp and save it in the user_master table in the record which is recently created.
       otp = randint(100000, 999999)
       recently_created_user = db.query(sql_alchemy_models.UserMaster).filter(sql_alchemy_models.UserMaster.id == new_user.id)
       #save otp in this newly created user
       recently_created_user.update({'account_activation_otp' : otp},synchronize_session=False)
       db.commit()

       title = 'Activate your account'
       name = new_user.email
       email_sent_to = new_user.email
       message1 = "please verify your email via otp to activate your account!"
       message2="Please ignore this mail if your account is already active."
       send_email_background(background_tasks, title,email_sent_to, {
        'title': title, 
        'name': name, 
        'otp':otp,
        'message1':message1,
        "message2":message2
        })
       response_data_dict = {
           'id':new_user.id,
           'email' : new_user.email,
           'is_blocked' : new_user.is_blocked,
           'is_deleted' : new_user.is_deleted,
           'created_at' : new_user.created_at
       }
       return response(status=status.HTTP_201_CREATED,message = DATA_INSERT_SUCCESS,data=response_data_dict)
    except Exception as e:
        print(f"create_users : {e}")
        return response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,error=e)

#verify otp that's sent to the user
@router.patch('/verify-otp')
def verify_otp(otpModel : VerifyOTPUsersModel, db : Session = Depends(db_flush)):
    try:
        otp_dict = otpModel.model_dump()
        otp_f = int(otp_dict.get('otp'))
        uid = int(otp_dict.get('id'))
        user = db.query(sql_alchemy_models.UserMaster).filter(sql_alchemy_models.UserMaster.id == uid, sql_alchemy_models.UserMaster.is_deleted == False)
        user_data = user.first()
        if not user_data:
            return response(status=status.HTTP_404_NOT_FOUND,error=DATA_NOT_FOUND_ERR)
        print(f"otp from db : {user_data.account_activation_otp}")
        print(f"otp from db : {uid}")
        if not user_data.is_blocked:
            return response(status=status.HTTP_400_BAD_REQUEST, error=USER_ACTIAVTED_ERR)
        if user_data.account_activation_otp == otp_f:
            user.update({'account_activation_otp':0, 'is_blocked':False},synchronize_session = False)
            db.commit()
            updated_user_data = user.first()
            response_data = {
                'id':updated_user_data.id,
                'email':updated_user_data.email,
                'is_blocked':updated_user_data.is_blocked,
                'is_deleted':updated_user_data.is_deleted,
                'created_at':updated_user_data.created_at
            }
            return response(status=status.HTTP_200_OK,message=OTP_VERIFICATION_SUCCESS,data=response_data)
        else:
            return response(status=status.HTTP_400_BAD_REQUEST,message=OTP_VERIFICATION_ERR)
    except Exception as e:
        print(f"verify_otp : {e}")
        return response(status=status.HTTP_500_INTERNAL_SERVER_ERROR, error=str(e))

#Resend otp to the user if requested by them
@router.patch('/send-mail/resend-otp/')
def resend_otp(resend_otp_model : ResendOtp, background_tasks : BackgroundTasks,db : Session = Depends(db_flush)):
    resend_otp_dict = resend_otp_model.model_dump()
    user_pk = resend_otp_dict.get('id')
    user = db.query(sql_alchemy_models.UserMaster).filter(sql_alchemy_models.UserMaster.id == user_pk, sql_alchemy_models.UserMaster.is_deleted == False)
    
    # create a new otp and then send it to the user's email address via Fastapi-email library
    new_user = user.first()
    if not new_user:
        return response(status=status.HTTP_404_NOT_FOUND,error=DATA_NOT_FOUND_ERR)
    if not new_user.is_blocked:
        return response(status=status.HTTP_400_BAD_REQUEST,error=USER_ACTIAVTED_ERR)
    #generate a new otp
    print(f"Old otp : {new_user.account_activation_otp}")
    otp = randint(100000,999999)
    #save the new otp in the database
    user.update({'account_activation_otp' : otp},synchronize_session = False)
    db.commit()
    #send otp via mail to the newly created user
    title = 'Activate your account'
    name = new_user.email
    email_sent_to = new_user.email
    message1 = "please verify your email via otp to activate your account!"
    message2 = "Please ignore this mail if your account is already active."
    send_email_background(background_tasks, title, email_sent_to, {
        'title':title,
        'name':name,
        'otp':otp,
        'message1':message1,
        'message2':message2
    })
    user_data = user.first()
    print(f"New otp : {user_data.account_activation_otp}")
    response_data = {
        'id':user_data.id,
        'email':user_data.email,
        'is_deleted': user_data.is_deleted,
        'is_blocked':user_data.is_blocked,
        'created_at':user_data.created_at
    }
    return response(status=status.HTTP_200_OK,message=MAIL_SENT_SUCCESS,data=response_data)

# Request a password change for the users whose account is activated
@router.patch('/send-mail/request-reset-password')
def request_reset_password(request_reset_password_model : RequestResetPasswordModel, background_tasks : BackgroundTasks, db : Session = Depends(db_flush)):
    request_reset_password_dictionary = request_reset_password_model.model_dump()
    email = request_reset_password_dictionary.get('email')
    users = db.query(sql_alchemy_models.UserMaster).filter(sql_alchemy_models.UserMaster.email == email, sql_alchemy_models.UserMaster.is_blocked == False, sql_alchemy_models.UserMaster.is_deleted == False)
    requested_user = users.first()
    if not requested_user:
        return response(status=status.HTTP_404_NOT_FOUND,error=DATA_NOT_FOUND_ERR)
    otp = randint(100000,999999)
    users.update({'account_activation_otp' : otp, 'verify_otp':True},synchronize_session = False)
    db.commit()
    title = 'Reset your password.'
    name = requested_user.email
    email_sent_to = requested_user.email
    message1 = "please verify your email via otp to reset your password!"
    message2 = "Please ignore this mail if you have already reset your password."
    send_email_background(background_tasks, title, email_sent_to, {
        'title':title,
        'name':name,
        'otp':otp,
        'message1':message1,
        'message2':message2
    })
    user_response_db = users.first()
    response_data = {
        'id':user_response_db.id,
        'email':user_response_db.email,
    }
    return response(status = status.HTTP_200_OK,message=MAIL_SENT_SUCCESS,data=response_data)

# Verify the otp generated for reset password
@router.patch('/verify-otp/reset-password')
def verify_otp_reset_password(reset_password_model : VerifyOTPUsersModel, db : Session = Depends(db_flush)):
    reset_password_dict = reset_password_model.model_dump()
    id = reset_password_dict.get('id')
    otp_f = reset_password_dict.get('otp')
    user = db.query(sql_alchemy_models.UserMaster).filter(sql_alchemy_models.UserMaster.id == id, sql_alchemy_models.UserMaster.is_blocked == False, sql_alchemy_models.UserMaster.verify_otp == True, sql_alchemy_models.UserMaster.account_activation_otp != 0, sql_alchemy_models.UserMaster.is_deleted == False)
    user_data = user.first()
    if not user_data:
        return response(status=status.HTTP_400_BAD_REQUEST,error=DATA_NOT_FOUND_ERR)
    if otp_f != user_data.account_activation_otp:
        return response(status=status.HTTP_400_BAD_REQUEST,error=OTP_VERIFICATION_ERR)
    user.update({'account_activation_otp':0},synchronize_session=False)
    db.commit()
    return response(status=status.HTTP_200_OK,message=OTP_VERIFICATION_SUCCESS)

# After otp verification allow user to reset his account's password
@router.patch('/reset-password')
def reset_password(reset_password_model : ResetPasswordModel, db:Session = Depends(db_flush)):
    reset_password_model_dict = reset_password_model.model_dump()
    id = reset_password_model_dict.get('id')
    password = reset_password_model_dict.get('password')
    password2 = reset_password_model_dict.get('password2')
    user = db.query(sql_alchemy_models.UserMaster).filter(sql_alchemy_models.UserMaster.id == id, sql_alchemy_models.UserMaster.account_activation_otp == 0, sql_alchemy_models.UserMaster.verify_otp == True, sql_alchemy_models.UserMaster.is_deleted == False)
    user_data = user.first()
    if not user_data:
        return response(status=status.HTTP_404_NOT_FOUND,message=DATA_NOT_FOUND_ERR)
    if password != password2:
        return response(status=status.HTTP_400_BAD_REQUEST,error=PASSWORD_MATCH_ERR)
    hash_reset_pass = hash_reset_pass_fun(password)
    user.update({'password':hash_reset_pass, 'verify_otp':False},synchronize_session=False)
    db.commit()
    return response(status=status.HTTP_200_OK,message=PASSWORD_RESET_SUCCESS)

# Create an api end-point that must return the logged in user's detail 
# If you are not able to access this api then your access token is expired and you need to get a new access token.
@router.get('/{id}')
def get_user_details(id : int, db : Session = Depends(db_flush)):
    user = db.query(sql_alchemy_models.UserMaster).filter(sql_alchemy_models.UserMaster.id == id, sql_alchemy_models.UserMaster.is_deleted == False).first()
    if not user:
        return response(status=status.HTTP_404_NOT_FOUND,error=DATA_NOT_FOUND_ERR)
    response_data = {
        'id':user.id,
        'email':user.email,
        'is_deleted':user.is_deleted,
        'is_blocked':user.is_blocked,
        'created_at':user.created_at
    }
    return response(status=status.HTTP_200_OK,message=DATA_SENT_SUCCESS,data=response_data)

# Login user

# Logout user     
