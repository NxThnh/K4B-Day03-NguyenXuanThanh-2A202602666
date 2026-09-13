# 📊 BÁO CÁO THU HOẠCH NGHIỆM THU BÀI LAB 3 (BƯỚC 3 — SUBMISSION ARTIFACT)

> **Họ và Tên Học viên:** Nguyễn Xuân Thành

> **Mã Sinh Viên / Mã Học viên:** 2A202602666

> **Chủ đề Lựa chọn:** *Trợ lý Kiểm định Chất lượng (QC Assistant):* Tra cứu ca lỗi gán nhãn 2D/3D và tạo phiếu Rework kiểm định.
---

## 1. BẢNG CHẤM ĐIỂM AGENTIC FIT SCORING MATRIX (ĐÁNH GIÁ CHỦ ĐỀ)

| Tiêu chí Đánh giá | Mức độ (1 - 5) |   Giải trình chi tiết lý do chọn điểm |
| :--- |  :---: | :--- |
| **1. Multi-step Reasoning** | **5 / 5** | Agent xác định mã lỗi và loại nhãn, tra cứu lịch sử/tiêu chuẩn, đánh giá mức độ ảnh hưởng rồi mới đề xuất hoặc tạo phiếu Rework. |
| **2. Tool Interaction** | **5 / 5** | Agent phải gọi Tool `query_defect_case` để lấy dữ liệu QC và `create_rework_ticket` để ghi nhận hành động vào hệ thống vận hành. |
| **3. Dynamic Decision** | **5 / 5** | Kết quả tra cứu quyết định bước tiếp theo: lỗi đủ điều kiện thì tạo Rework, thiếu dữ liệu thì hỏi bổ sung, còn mã không tồn tại thì dừng và thông báo rõ ràng. |
| **4. Long Horizon Goal** | **4 / 5** | Agent duy trì mục tiêu xử lý ca lỗi từ tra cứu đến hoàn tất phiếu Rework; điểm chưa tối đa vì quy trình mẫu thường hoàn tất trong một phiên. |
| **TỔNG ĐIỂM AGENTIC FIT** | **19 / 20** | *Tổng điểm > 12/20, vì vậy QC Assistant rất phù hợp để triển khai dưới dạng Agentic System.* |

---

## 2. TRÍCH XUẤT KẾT QUẢ WATERFALL TRACE LOG (SAU KHI CHẠY TEST SUITE TRÊN API THẬT)

> ⚠️ **YÊU CẦU NGHIỆM THU:** Mở tệp `.env` điền `GEMINI_API_KEY` (hoặc `OPENAI_API_KEY`) để kết nối LLM thật trước khi thực thi `python src/app.py --all`. Bài nộp chỉ dùng Mock Offline Provider sẽ không đạt điểm nghiệm thực tế.

Dưới đây là đoạn trích xuất tiêu biểu từ file `docs/trace_waterfall.json`, thể hiện Agent tra cứu ca lỗi và tạo phiếu Rework:

```json
[
  {
    "step": 1,
    "query": "Hãy tra cứu ca lỗi gán nhãn 2D QC-2D-014.",
    "action_type": "TOOL_EXECUTION",
    "tool_name": "query_defect_case",
    "arguments": {
      "defect_code": "QC-2D-014"
    },
    "observation": {
      "status": "SUCCESS",
      "defect_code": "QC-2D-014",
      "data": {
        "label_type": "2D",
        "lot_code": "VF8-2026-0913",
        "severity": "Cao",
        "rework_required": true
      }
    },
    "latency_ms": 0.0
  },
  {
    "step": 1,
    "query": "Hãy tạo phiếu Rework cho ca lỗi QC-2D-014.",
    "action_type": "TOOL_EXECUTION",
    "tool_name": "create_rework_ticket",
    "arguments": {
      "defect_code": "QC-2D-014",
      "lot_code": "VF8-2026-0913",
      "assignee": "Nguyễn Minh"
    },
    "observation": {
      "status": "SUCCESS",
      "ticket_id": "RW-QC-2D-014-01"
    },
    "latency_ms": 0.0
  },
  {
    "step": 2,
    "query": "Hãy tạo phiếu Rework cho ca lỗi QC-2D-014.",
    "action_type": "FINAL_ANSWER",
    "thought": "Tổng hợp kết quả từ MCP Server thành công.",
    "output": "Đã tạo phiếu Rework cho ca lỗi QC-2D-014, giao cho Nguyễn Minh.",
    "latency_ms": 10.0
  }
]
```

---

## 3. TỔNG KẾT KẾT QUẢ NGHIỆM THU & NỘP BÀI

- [x] Đã điền API Key thật trong `.env` và xác nhận Agent chạy mượt mà trên LLM API thật (Gemini/OpenAI).
- **Tổng số Test Cases đã chạy thành công:** **5 / 5 test cases**.
- **Số lượt gọi Tool qua MCP Server chính xác:** **5 lượt** (TC02: 1, TC03: 1, TC04: 2, TC05: 1).
- **Kết quả đẩy Repo nộp bài:** [x] Đã Commit và Push mã nguồn thành công lên GitHub cá nhân.

---

> ✅ **HOÀN TẤT NỘP BÀI:** Sao chép đường link GitHub Repository cá nhân của bạn và dán vào ô nộp bài trên hệ thống LMS VLearn để hoàn tất Bài Lab 3!
