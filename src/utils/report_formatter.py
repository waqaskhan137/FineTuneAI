class ReportFormatter:
    def __init__(self):
        self.sections = []

    def add_section(self, title, description, content):
        section = {
            "title": title,
            "description": description,
            "content": content
        }
        self.sections.append(section)

    def get_report(self):
        report_lines = []
        for section in self.sections:
            report_lines.append(f"# {section['title']}\n")
            report_lines.append(f"{section['description']}\n")
            report_lines.append(f"{section['content']}\n")
            report_lines.append("\n---\n")
        return "\n".join(report_lines) 