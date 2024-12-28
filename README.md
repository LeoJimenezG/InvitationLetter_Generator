# Invitation Letter Generator ✉️

A program to create personalized invitation letters using a template and a list of names.

---

## 📘 How Does It Work?

### 1. Input Names:
   - The program reads names from a file named `names_list.txt`.  
   - File path: `./input/names/names_list.txt`.
   - You can include as many names as you'd like in this file. But make sure to maintain the format.

2. **Template Customization**:
   - The invitation letter is based on a customizable template.  
   - **Important**: Ensure the template contains the keyword `[name]`.  
   - The program will replace `[name]` with each of the names from `names_list.txt`.

3. **Output Letters**:
   - The program generates a personalized invitation for each name in the list.  
   - All generated letters are saved in the `ready_letters` directory.  
   - Output path: `./output/ready_letters`.

---

## 💡 Notes

- You can modify the letter template as needed, but the placeholder `[name]` is **required**.  
- Each invitation letter is automatically saved and ready to use!
