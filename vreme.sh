_vreme() {
   local cur opts
	COMPREPLY=()
	cur="${COMP_WORDS[COMP_CWORD]}"
	if [[ -f /tmp/vreme ]]; then
		opts=$(</tmp/vreme)
	else
		opts="$(vreme -c)"
		echo >/tmp/vreme "${opts}"
	fi
	COMPREPLY=( $(compgen -W "${opts}" -- ${cur}) )
}
complete -F _vreme vreme 
