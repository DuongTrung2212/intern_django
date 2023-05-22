from django.shortcuts import render
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas


# Create your views here.
def some_view(request):
    # Tạo bộ đệm giống như tệp để nhận dữ liệu PDF.
    buffer = io.BytesIO()

    # Tạo đối tượng PDF, sử dụng bộ đệm làm đối tượng"file"
    p = canvas.Canvas(buffer)
    p.bookmarkPage("My bookmap")
    p.setTitle("Title")
    p.drawString(0, 0, "<h1>Hello World!</h1>.")
    p.showPage()
    p.save()
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=False, filename="hello.pdf")
