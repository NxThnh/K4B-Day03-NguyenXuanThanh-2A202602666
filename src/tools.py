"""Tool schemas and execution backend for the QC Assistant."""

import json
from typing import Any, Dict

TOOLS_SCHEMA = [
    {
        "name": "query_defect_case",
        "description": "Tra cứu ca lỗi kiểm định gán nhãn 2D/3D theo mã lỗi.",
        "parameters": {
            "type": "object",
            "properties": {
                "defect_code": {
                    "type": "string",
                    "description": "Mã ca lỗi, ví dụ QC-2D-014"
                }
            },
            "required": ["defect_code"]
        }
    },
    {
        "name": "create_rework_ticket",
        "description": "Tạo phiếu Rework cho ca lỗi đã được xác nhận.",
        "parameters": {
            "type": "object",
            "properties": {
                "defect_code": {
                    "type": "string",
                    "description": "Mã ca lỗi cần xử lý"
                },
                "lot_code": {
                    "type": "string",
                    "description": "Mã lô sản xuất"
                },
                "assignee": {
                    "type": "string",
                    "description": "Người phụ trách Rework"
                }
            },
            "required": ["defect_code", "lot_code", "assignee"]
        }
    }
]

MOCK_DATABASE = {
    "QC-2D-014": {
        "label_type": "2D",
        "lot_code": "VF8-2026-0913",
        "severity": "Cao",
        "status": "CONFIRMED",
        "rework_required": True,
        "description": "Nhãn 2D bị lệch vùng đọc."
    },
    "QC-3D-027": {
        "label_type": "3D",
        "lot_code": "VF9-2026-0913",
        "severity": "Cao",
        "status": "CONFIRMED",
        "rework_required": True,
        "description": "Mã 3D không đọc được ở nhiều sản phẩm."
    }
}


def execute_query_defect_case(defect_code: str) -> str:
    normalized_code = defect_code.strip().upper()
    defect = MOCK_DATABASE.get(normalized_code)
    if defect is None:
        return json.dumps({
            "status": "NOT_FOUND",
            "message": f"Không tìm thấy ca lỗi kiểm định có mã '{defect_code}'."
        }, ensure_ascii=False)
    return json.dumps({
        "status": "SUCCESS",
        "defect_code": normalized_code,
        "data": defect
    }, ensure_ascii=False)


def execute_create_rework_ticket(
    defect_code: str, lot_code: str, assignee: str
) -> str:
    normalized_code = defect_code.strip().upper()
    defect = MOCK_DATABASE.get(normalized_code)
    if defect is None:
        return json.dumps({
            "status": "NOT_FOUND",
            "message": f"Không thể tạo Rework vì không tìm thấy ca lỗi '{defect_code}'."
        }, ensure_ascii=False)
    if not defect["rework_required"]:
        return json.dumps({
            "status": "REWORK_NOT_REQUIRED",
            "message": f"Ca lỗi {normalized_code} chưa đủ điều kiện tạo phiếu Rework."
        }, ensure_ascii=False)
    return json.dumps({
        "status": "SUCCESS",
        "ticket_id": f"RW-{normalized_code}-01",
        "defect_code": normalized_code,
        "lot_code": lot_code,
        "assignee": assignee,
        "message": f"Đã tạo phiếu Rework cho ca lỗi {normalized_code}, giao cho {assignee}."
    }, ensure_ascii=False)


TOOL_ROUTER = {
    "query_defect_case": execute_query_defect_case,
    "create_rework_ticket": execute_create_rework_ticket
}


def dispatch_tool_call(tool_name: str, arguments: Dict[str, Any]) -> str:
    """Dispatch a tool call and return a JSON-encoded result."""
    if tool_name not in TOOL_ROUTER:
        return json.dumps({
            "status": "UNKNOWN_TOOL",
            "error": f"Tool '{tool_name}' không tồn tại!"
        }, ensure_ascii=False)
    try:
        return TOOL_ROUTER[tool_name](**arguments)
    except Exception as exc:
        return json.dumps({
            "status": "EXECUTION_ERROR",
            "error": str(exc)
        }, ensure_ascii=False)
