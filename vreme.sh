_vreme() {
   local cur opts
	COMPREPLY=()
	cur="${COMP_WORDS[COMP_CWORD]}"
    opts="Novi_sad Beograd"
	COMPREPLY=( $(compgen -W "${opts}" -- ${cur}) )
}
complete -F _vreme vreme 
