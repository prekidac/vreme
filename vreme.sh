_vreme() {
   local cur opts
	COMPREPLY=()
	cur="${COMP_WORDS[COMP_CWORD]}"
	if [[ -f /tmp/vreme ]]; then
		mapfile -t </tmp/vreme opts
		if [[ "${opts[0]}" == "$(date -d '')" ]]; then
			opts="${opts[1]}"
		else
			opts="$(vreme -c)" || return 0
			echo >/tmp/vreme $(date -d '')
			echo >>/tmp/vreme "${opts}"
		fi
	else
		opts="$(vreme -c)" || return 0
		echo >/tmp/vreme $(date -d '')
		echo >>/tmp/vreme "${opts}"
	fi
	COMPREPLY=( $(compgen -W "${opts}" -- ${cur^}) )
}
complete -F _vreme vreme 
