#include <sys/stat.h>
#include <unistd.h>
#include <fcntl.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>


#define BUF_SIZE 8192

int main(int argc , char* argv[])
{
	if (argc!=2)
  {
  	fprintf(stderr,"Usage: lstat_stat file1 ");
  	return 1;
  }
  
	char buf;
	int size,fd;

	fd = open(argv[1],O_RDONLY);
	size = lseek(fd,-1,SEEK_END);
	while(size-- >= 0 )
	{
		read (fd,&buf,1);
		write(STDOUT_FILENO,&buf,1);
		lseek(fd,-2,SEEK_CUR);

	}
	return 0;
}