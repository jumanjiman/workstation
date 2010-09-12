if [ -n "$BASH_VERSION" -o -n "$KSH_VERSION" -o -n "$ZSH_VERSION" ]; then
  test -n "$INPUTRC" || export INPUTRC="$HOME/.etc/inputrc"
  test -d "$HOME/.etc" || mkdir -p "$HOME/.etc" &> /dev/null
  test -f "$HOME/.etc/inputrc" || cat > "$HOME/.etc/inputrc" <<- EOF
	set editing-mode vi
	#set editing-mode emacs
	EOF
fi
