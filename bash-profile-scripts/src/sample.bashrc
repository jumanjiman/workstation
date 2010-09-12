# .bashrc

# Source global definitions
if [ -f /etc/bashrc ]; then
	. /etc/bashrc
fi

# override global settings here



# use text-mode browser whenever possible
export BROWSER="elinks"

# always use ssh for rsync'ing
export RSYNC_RSH="ssh"

# set my preferred printer for command-line stuff
# sysV-style
#export PRINTER="printername"
# bsd-style
#export LPDEST="$PRINTER"

# set my proxy pref's
#export HTTP_PROXY="http://username:password@host:port"
#export FTP_PROXY="$HTTP_PROXY"

# some programs expect proxy in lower-case
#export http_proxy="$HTTP_PROXY"
#export ftp_proxy="$FTP_PROXY"

# automatically log out of a shell after 300 seconds of idle time
#export TMOUT=300
