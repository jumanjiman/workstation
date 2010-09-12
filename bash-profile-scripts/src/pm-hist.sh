if [ -n "$BASH_VERSION" -o -n "$KSH_VERSION" -o -n "$ZSH_VERSION" ]; then
  # assign history variables
  export HISTIGNORE="&"
  export HISTSIZE=999888
  export HISTFILESIZE=$HISTSIZE
  export HISTTIMEFORMAT='%F %T '
  shopt -s histappend
fi
