======》内容：正则表达式基础

1. 通配符：句点与其他除换行符之外的符号都匹配
2. 对特殊字符进行转义 
   如何python.py 对句点进行转义 r'python\.py'  或者
   python\\.py 双斜杠的解释 解释器的转义和re模块的转义
3. 字符集：字符集一次只能匹配一个字符 
   [a-zA-Z0-9] 所有英文无论大小写 0-9的数字都匹配
   [^abc] 排除abc之外的所有字符
4.（ | ） 二选一
   'python|perl'
5. (pattern)? 在子模块后面加上问号 将其变为可选的 及可有可无
   (pattern)* 可重复0 , 1 ，多次
   (pattern)+ 可重复 1，多次
   (pattern){m,n} 可重复m~n次
6.字符串的开头和结尾进行匹配
  '^ht+p' 必须ht+p开头
  'com$'  以com结尾
   
======》Python中re模块的内容 操作正则表达式

compile(pattern[, flags]) 根据正则表达式的字符串创建模块
search(pattern, string[, flags]) 在字符串中查找模块
match(pattern, string[, flags]) 在字符串头匹配模式
split(pattern, string[, maxsplit=0]) 根据模式来分割字符串
findall(pattern, string) 返回一个列表 包含所有匹配字符串
sub(pat, repl, string[, count=0]) 将字符串中与模式pat匹配的字符串都替换为repl
escape(string) 对字符串中所有正则表达式都转义

re.search(pat, string) pat正则表达式字符串
使用compile对正则表达式进行转换后 以后不需要再进行转换
pat=re.compile(pattern)
pat.search(string)
