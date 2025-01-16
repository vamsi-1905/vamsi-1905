#include<stdio.h>
int main()
{
    int m,pin,x,lpin,choice=0,temp1,newpin,response;
    long long int money,accountnumber,luser,depo,withdraw,lmoney;
    printf("Welcome to amrita bank\n");
    printf("enter the number of users\n");
    scanf("%d",&m);
    int accounts[m][3];
    for(int i=0;i<m;i++){
        for(int j=0;j<3;j++){
            x=j;
            if(x==0){
                printf("enter the account number \n");
                scanf("%lld",&accountnumber);
                accounts[i][j]=accountnumber;
            }
            else if(x==1){
                printf("enter the pin\n");
                scanf("%d",&pin);
                accounts[i][j]=pin;
            }
            else if(x==2){
                printf("enter the money\n");
                scanf("%lld",&money);
                accounts[i][j]=money;
                break;
            }
            else{
                printf("invalid\n");
            }

        }
    }

    printf("enter your accountnumber to login\n");
    scanf("%lld",&luser);
    if(luser!=accountnumber)
    printf("Account doesnt exist\n");
    else{
    printf("now enter your pin to login\n");
    scanf("%d",&lpin);
    int flag=0;
    for(int i=0;i<m;i++){
            if(accounts[i][0]==luser && accounts[i][1]==lpin){
                lmoney=accounts[i][2];
                temp1=i;
                flag=1;
                printf("Successfully logged in\n");
            }
            else if(accounts[i][0]==luser && accounts[i][1]!=lpin){
                printf("invalid pin\n");
                break;
            }
            else {
                printf("Account doesnt exist\n");
            }
    }


           if(flag==1){
            printf(" what would you like to do\n");
            while(choice!=5){
            printf("1) show money\n");
            printf("2) deposit money\n");
            printf("3) withdraw money\n");
            printf("4) pin change\n");
            printf("5) logout\n");
            scanf("%d",&choice);
            if(choice==1){
                printf("you have %lld amount of money in your account\n",lmoney);
            }
            else if(choice==2){
                printf("how much money do you want to deposit\n");
                scanf("%lld",&depo);
                lmoney=lmoney+depo;
                accounts[temp1][2]=lmoney;
                printf("you have succesfully deposited %lld to your acount\n",depo);
                printf("now you have %lld\n",lmoney);
            }
            else if(choice==3){
                if(lmoney>=500){
                    printf("enter amount to be withdrawn\n");
                    scanf("%lld",&withdraw);
                    if(lmoney-withdraw>=500){
                        lmoney=lmoney-withdraw;
                        printf("you have withdrawn %lld\n",withdraw);
                        printf("now you have %lld  amount left\n",lmoney);
                    }
                    else{
                        printf("amount not sufficient\n");
                    }
                }
            }
            else if(choice==4){
                printf("enter old pin \n");
                scanf("%d",&lpin);
                if(lpin==accounts[temp1][1]){
                    printf("enter the new pin \n");
                    scanf("%d",&newpin);
                    pin=newpin;
                    if(newpin==accounts[temp1][1])
                    {
                        printf("Old password not allowed\n");
                        break;
                    }
                    else
                    {
                    printf("renter the new pin\n");
                    scanf("%d",&newpin);
                    if(pin==newpin){
                        printf("pin changed succesfully\n");
                        accounts[temp1][1]=newpin;
                    }
                     else if(pin==newpin){
                        printf("pin not matching\n");
                    }

                }
                        printf("Would you like to login again?\n");
                        printf("Press 1 for yes and 0 for no\n");
                        scanf("%d",&response);
                        if(response==1)
                        {
                             printf("enter your accountnumber to login\n");
                              scanf("%lld",&luser);
                              if(luser!=accountnumber)
                              printf("Account doesnt exist\n");
                              else{
                              printf("now enter your pin to login\n");
                             scanf("%d",&lpin);
                              flag=0;
                             for(int i=0;i<m;i++){
                              if(accounts[i][0]==luser && accounts[i][1]==lpin){
                                lmoney=accounts[i][2];
                                  temp1=i;
                                  flag=1;
                                   printf("Successfully logged in\n");
                              }
                                  else if(accounts[i][0]==luser && accounts[i][1]!=lpin){
                                printf("invalid pin\n");
                                break;
                                }
                                else {
                               printf("Account doesnt exist\n");
                            }

                        }
                    }
                        }

            }
            else if(choice==5){
                printf("You have succesfully logged out,Thank you for using amrita bank\n");
                luser=0;
                lpin=0;
                pin=0;
                temp1=0;
                break;

            }
            else{
                printf("invalid choice , should be between 1 to 5");
            }


        }
    }
}
}
}
