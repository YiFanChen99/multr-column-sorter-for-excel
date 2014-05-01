# -*- coding:utf-8 -*-

import TableBuilder

table = TableBuilder.build_table()
table.sort(key=lambda x: [x[3], x[4]])

print '\n'.join(['\t'.join(row) for row in table])
