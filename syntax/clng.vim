" Vim syntax file
" Language: clng
" Usage:
"   Place this file in .vim/syntax/clng.vim
"   and add into your .vimrc file the following:
"   autocmd BufRead,BufNewFile *.clng set filetype=clng

if exists('b:current_syntax')
    finish
endif

set iskeyword=a-z,A-Z,=,@,!
syntax keyword clngTodos TODO FIXME NOTE URGENT

syntax keyword clngKeywords category symbol shape syllable load list

syntax region clngCommentLine start='#' end='$' contains=clngTodos

syntax region clngNumber start=/\s\d/ skip=/\d/ end=/(\s|\D)/

highlight default link clngTodos Todo
highlight default link clngKeywords Keyword
highlight default link clngCommentLine Comment
highlight default link clngNumber Number

let b:current_syntax = 'clng'

