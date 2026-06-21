from datetime import date
from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer


# func wuxu sameyn .pdf report 
def generate_report(manager):
    today = str(date.today())

    total_students = len(manager.students)
    total_drivers = len(manager.drivers)
    total_buses = len(manager.buses)

    total_fees = sum(s.fee for s in manager.students)
    total_salary = sum(d.salary for d in manager.drivers)
    balance = total_fees - total_salary # Lacagta soo harta marka mushaarka laga jaro


    # ---------------- PDF REPORT (Professional Version) ----------------
    pdf_file = "report.pdf"
    
    # Waxaan isticmaalaynaa Landscape (Ballaaran) si xogta oo dhami u wada gasho
    doc = SimpleDocTemplate(pdf_file, pagesize=landscape(letter), rightMargin=30, leftMargin=30, topMargin=30, bottomMargin=30)
    elements = []
    styles = getSampleStyleSheet()

    # Styles-ka
    title_style = ParagraphStyle(
        name='TitleStyle',
        parent=styles['Heading1'],
        fontSize=24,
        textColor=colors.HexColor("#1A237E"),
        alignment=1,
        spaceAfter=15
    )

    subtitle_style = ParagraphStyle(
        name='SubtitleStyle',
        parent=styles['Heading2'],
        fontSize=14,
        textColor=colors.HexColor("#333333"),
        spaceAfter=10,
        spaceBefore=20
    )

    # Header
    elements.append(Paragraph("<b>BUS SCHOOL MANAGEMENT REPORT</b>", title_style))
    elements.append(Paragraph(f"<b>Generated Date:</b> {today}", styles['Normal']))
    elements.append(Spacer(1, 10))

    # --- 1. Jadwalka Ardayda (Students Table) ---
    if manager.students:
        elements.append(Paragraph("<b>1. Registered Students</b>", subtitle_style))
        student_data = [["ID", "Full Name", "Gender", "Class", "Parent Name", "Phone", "Fee ($)", "Driver"]]
        
        for s in manager.students:
            student_data.append([str(s.id), s.fullname, s.gender, s.student_class, s.parent_name, s.parent_phone, f"${s.fee}", s.driver])

        student_table = Table(student_data, colWidths=[30, 130, 60, 80, 130, 100, 60, 100])
        student_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#3F51B5")), 
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 10),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
            ('BACKGROUND', (0, 1), (-1, -1), colors.HexColor("#E8EAF6")),
            ('GRID', (0, 0), (-1, -1), 1, colors.white),
            ('FONTSIZE', (0, 1), (-1, -1), 9), # Font-ga ardayda waa yaraayay si uu u wada galo
        ]))
        elements.append(student_table)

    # --- 2. Jadwalka Darawalada (Drivers Table) ---
    if manager.drivers:
        elements.append(Paragraph("<b>2. Registered Drivers</b>", subtitle_style))
        driver_data = [["ID", "Full Name", "Phone", "License No.", "Salary ($)"]]
        
        for d in manager.drivers:
            driver_data.append([str(d.id), d.fullname, d.phone, d.license_number, f"${d.salary}"])

        driver_table = Table(driver_data, colWidths=[40, 180, 120, 120, 100])
        driver_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#00695C")),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
            ('BACKGROUND', (0, 1), (-1, -1), colors.HexColor("#E0F2F1")),
            ('GRID', (0, 0), (-1, -1), 1, colors.white),
        ]))
        elements.append(driver_table)

    # --- 3. Jadwalka Basaska (Buses Table) ---
    if manager.buses:
        elements.append(Paragraph("<b>3. Registered Buses</b>", subtitle_style))
        bus_data = [["ID", "Bus Number", "Capacity", "Assigned Driver"]]
        
        for b in manager.buses:
            bus_data.append([str(b.id), b.bus_number, str(b.capacity), b.driver])

        bus_table = Table(bus_data, colWidths=[40, 150, 100, 180])
        bus_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#E64A19")), # Midab Liimi (Orange) Ah
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
            ('BACKGROUND', (0, 1), (-1, -1), colors.HexColor("#FBE9E7")),
            ('GRID', (0, 0), (-1, -1), 1, colors.white),
        ]))
        elements.append(bus_table)

    # --- 4. Xisaabta Guud (Financial Summary) ---
    elements.append(Spacer(1, 20))
    elements.append(Paragraph("<b>4. Overall Summary</b>", subtitle_style))

    summary_data = [
        ["DESCRIPTION", "COUNT / AMOUNT"],
        ["Total Students", str(total_students)],
        ["Total Drivers", str(total_drivers)],
        ["Total Buses", str(total_buses)],
        ["Total Fees Collected (Income)", f"${total_fees}"],
        ["Total Salaries (Expense)", f"${total_salary}"],
        ["NET BALANCE (Profit)", f"${balance}"]
    ]

    summary_table = Table(summary_data, colWidths=[250, 150])
    summary_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#424242")),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (0, -1), 'LEFT'),
        ('ALIGN', (1, 0), (1, -1), 'RIGHT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 11),
        ('PADDING', (0, 0), (-1, -1), 8),
        ('BACKGROUND', (0, 1), (-1, -1), colors.HexColor("#F5F5F5")),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.silver),
        ('FONTNAME', (0, -1), (-1, -1), 'Helvetica-Bold'), 
        ('BACKGROUND', (0, -1), (-1, -1), colors.HexColor("#E0E0E0")), # Net balance color
    ]))
    elements.append(summary_table)

    # Generate the PDF
    doc.build(elements)

    print("\n[+] Success: Reports generated completely (report.txt + report.pdf)!")