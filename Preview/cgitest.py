# 主html模板
fieldnames = ('name', 'age', 'job', 'pay')
replyhtml = """
<html>
<title>People Input Form</title>
<body>
<form method=POST action="cgi-bin/peoplecgi.py">
    <table>
    <tr><th>Key <td><input type=text name=key value="%(key)s">
    $ROWS$
    </table>
    <P>
    <input type=submit value="Fetch", name=action>
    <input type=submit value="Update", name=action>
</form>
</body>
</html>
"""

# 为$ROW$的数据行插入html
rowhtml = '<tr><th>%s<td><input type=text name=%s value="%%(%s)s">\n'
rowshtml = ''
for fieldname in fieldnames:
    rowshtml += (rowhtml % ((fieldname,) * 3))
    print(rowshtml)
    print('\n$$$$$$$$$$$$\n')
print(replyhtml)
replyhtml = replyhtml.replace('$ROWS$', rowshtml)
print('\n$$$$$$$$$$$$\n')
print(replyhtml)
