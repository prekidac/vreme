_vreme() {
   local cur prev opts
	COMPREPLY=()
	cur="${COMP_WORDS[COMP_CWORD]}"
    opts=( $(vreme -c) )

	if [[ ${COMP_CWORD} -eq 1 ]] ; then
		COMPREPLY=( $(compgen -W "${opts[@]}" -- ${cur}) )
		return 0
	fi
}
complete -F _vreme vreme 