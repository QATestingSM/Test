from box import Box
import re
from typing import List, Tuple
from modules.validators import validate_table_operation, validate_tables, validate_columns, validate_conditions, validate_function, validate_where_placeholders

ALLOWED_TABLES = [
    "[demo_api].[dbo].[profiles]",
    "[demo_api].[dbo].[orders]",
    "[demo_api].[dbo].[products]",
    "[demo_api].[dbo].[testingtable]"
]
    
class FormatterAgent:
    def __init__(self):
        pass
    
    def _format_query(self, query, table, operation, **kwargs):
        return query.format(table=table, **kwargs)
    
    def format_select(self, table, columns="*", where=None, order_by=None):
        if not columns:
            columns = "*"
        
        parts = [f"SELECT {columns} FROM {table}"]
        format_kwargs = {"columns": columns}
        
        if where:
            parts.append("WHERE {where}")
            format_kwargs["where"] = where
        
        if order_by:
            parts.append("ORDER BY {order_by}")
            format_kwargs["order_by"] = order_by
        
        query_template = " ".join(parts)
        
        return self._format_query(query_template, table, operation="SELECT", **format_kwargs)