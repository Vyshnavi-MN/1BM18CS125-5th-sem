#include<stdio.h>
#include<stdlib.h>
#include<string.h>

//Change the 16 bit polynomial to the required value, Below is a considered value
// For test provide 1101 as input 

char g[]="1000100000010001",p[50],c[50];
int n1,n2;

void xor()
{
	int i;
	for(i=0;i<n1;i++)
	{
		if(c[i]==g[i])
		{
			c[i]='0';
		}
		else
		{
			c[i]='1';
		}
	}
}

void crc()
{
	int i,count;
	for(count=0;count<n1;count++)
	{
		c[count]=p[count];
	}
	do
	{
		 if(c[0]=='1')
		 {
			 xor();
		 }
		 for(i=0;i<n1-1;i++)
		 {
			 c[i]=c[i+1];
		 }
		 c[i]=p[count++];
	 }while(count<n2+n1);
 }

void main()
{
	int i;
	printf("Enter your code\n");
	scanf("%s",p);
	n1=strlen(g);
	n2=strlen(p);
	for(i=n2;i<n2+n1;i++)
	{
		p[i]='0';
	}
	crc();
	printf("Checksum : %s\n",p);
	printf("Current code : %s\n",g);
	for(i=n2;i<n2+n1;i++)
	{
		p[i]=c[i-n2];
	}
	printf("Transmitted code : %s\n",p);
	//give the above output(transmitted code itself) as input to (re enter code) get no error
	//If an error has to occur change the above output and provide the input
	    
	printf("The code transmitted is : %s\n",p);
	scanf("%s",p);
	crc();
	for(i=0;i<strlen(c);i++)
	{
		if(c[i]=='1')
		{
			printf("Error found\n");
			exit(0);
		}
	}
	printf("no error\n");
}