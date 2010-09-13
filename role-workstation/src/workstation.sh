#!/bin/bash

# this script configures the workstation environment via gconftool-2

function apply_gconf() {
  # applies all configs from a file
  [[ -n $1 ]] || return 1
  [[ -r $1 ]] || return 2
  # open $1 for reading
  exec 3< $1

  while read <&3; do
    # blank line is a noop
    [[ -n $REPLY ]] || continue

    # line beginning with # is a noop
    grep -q '^[[:space:]]*#' <<< $REPLY && continue
    
    errors=$(/usr/bin/gconftool-2 --set $REPLY 2>&1)
    /usr/bin/logger -t role-workstation "$errors"
  done

  # close fd
  exec 3<-
}

global_gconf=/etc/role-workstation/gconf-keys.conf
user_gconf=$HOME/.etc/role-workstation/gconf-keys.conf
global_config=/etc/role-workstation/workstation.conf
user_config=$HOME/.etc/role-workstation/workstation.conf

apply_gconf $global_gconf
apply_gconf $user_gconf

