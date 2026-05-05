import os
import json
from datetime import datetime

def get_skill_status():
    skills_dir = os.path.join(os.getcwd(), ".claude", "skills")
    if not os.path.exists(skills_dir):
        return "No skills found."
    
    report = ["# Reflection Status\n"]
    skills = [d for d in os.listdir(skills_dir) if os.path.isdir(os.path.join(skills_dir, d))]
    
    for skill in skills:
        skill_path = os.path.join(skills_dir, skill)
        skill_md = os.path.join(skill_path, "SKILL.md")
        
        status = "Active"
        last_modified = datetime.fromtimestamp(os.path.getmtime(skill_path)).strftime('%Y-%m-%d %H:%M')
        
        report.append(f"- **{skill}**: {status} (Last evolved: {last_modified})")
        
    return "\n".join(report)

if __name__ == "__main__":
    print(get_skill_status())
