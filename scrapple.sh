
_scrapple()
{
    local cur
    cur="${COMP_WORDS[COMP_CWORD]}"

    if [ $COMP_CWORD -eq 1 ]; then
        COMPREPLY=( $( compgen -W '-h --help -h --help -V --version run genconfig generate' -- $cur) )
    else
        case ${COMP_WORDS[1]} in
            run)
            _scrapple_run
        ;;
            genconfig)
            _scrapple_genconfig
        ;;
            generate)
            _scrapple_generate
        ;;
        esac

    fi
}

_scrapple_run()
{
    local cur
    cur="${COMP_WORDS[COMP_CWORD]}"

    if [ $COMP_CWORD -ge 2 ]; then
        COMPREPLY=( $( compgen -fW '-o= --output_type= -v= --verbosity= ' -- $cur) )
    fi
}

_scrapple_genconfig()
{
    local cur
    cur="${COMP_WORDS[COMP_CWORD]}"

    if [ $COMP_CWORD -ge 2 ]; then
        COMPREPLY=( $( compgen -fW '-t= --type= -s= --selector= -l= --levels= ' -- $cur) )
    fi
}

_scrapple_generate()
{
    local cur
    cur="${COMP_WORDS[COMP_CWORD]}"

    if [ $COMP_CWORD -ge 2 ]; then
        COMPREPLY=( $( compgen -fW '-o= --output_type= ' -- $cur) )
    fi
}

complete -o bashdefault -o default -o filenames -F _scrapple scrapple