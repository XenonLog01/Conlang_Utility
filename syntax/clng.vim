" Vim syntax file
" Language: clng

if exists('b:current_syntax')
    finish
endif

set iskeyword=a-z,A-Z,=,@,!
syntax keyword clngTodos TODO FIXME NOTE URGENT

syntax keyword clngKeywords category symbol shape syllable 

syntax region clngCommentLine start='#' end='$' contains=clngTodos

syntax region clngNumber start=/\s\d/ skip=/\d/ end=/\s/

highlight default link clngTodos Todo
highlight default link clngKeywords Keyword
highlight default link clngCommentLine Comment
highlight default link clngNumber Number

let b:current_syntax = 'clng'

