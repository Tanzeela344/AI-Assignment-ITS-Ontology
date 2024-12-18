import tkinter as tk
from tkinter import messagebox
from shapes import calculate_area
from lessons import lessons
from database import update_progress, fetch_progress

import numpy as np

# Theme colors
BG_COLOR = "#F4F6F6"  # Light background color
BUTTON_COLOR = "#3498db"  # Blue button color
BUTTON_HOVER_COLOR = "#2980b9"  # Darker hover color
TEXT_COLOR = "#2c3e50"  # Text color
HEADING_COLOR = "#e74c3c"  # Red heading color
EXIT_BUTTON_COLOR = "#e74c3c"  # Red exit button color


def show_lesson(shape):
    lesson = lessons[shape]
    top = tk.Toplevel()
    top.configure(bg=BG_COLOR)
    top.title(f"{shape} Lesson")
    top.geometry("800x700")  
    top.resizable(False, False)

    # Display lesson title
    tk.Label(top, text=f"Learn about {shape}!", font=("Arial", 22, "bold"), fg=HEADING_COLOR, bg=BG_COLOR).pack(pady=20)

    # Display formula and example
    tk.Label(top, text=f"Formula: {lesson['formula']}", font=("Arial", 16), fg=TEXT_COLOR, bg=BG_COLOR).pack(pady=10)
    tk.Label(top, text=f"Example: {lesson['example']}", font=("Arial", 14), fg=TEXT_COLOR, bg=BG_COLOR).pack(pady=10)

    # Display image
    image_path = lesson["image"]
    img = tk.PhotoImage(file=image_path)
    image_label = tk.Label(top, image=img, bg=BG_COLOR)
    image_label.image = img  
    image_label.pack(pady=10)

    tk.Button(top, text="Close", command=top.destroy,
              bg=EXIT_BUTTON_COLOR, fg="white", font=("Arial", 12, "bold"),
              padx=10, pady=5).pack(pady=20)


def ask_question(shape):
    lesson = lessons[shape]
    question = lesson['questions'][0]

    def check_answer():
        try:
            user_answer = float(answer_entry.get())
            correct_answer = calculate_area(shape, **question)
            if abs(user_answer - correct_answer) < 0.01:
                update_progress("Student", shape, 10)
                messagebox.showinfo("Result", "🎉 Correct! Well done!")
            else:
                messagebox.showinfo("Result", f"❌ Incorrect! The correct answer is {correct_answer:.2f}")
            answer_entry.delete(0, tk.END)  # Clear the input field
        except ValueError:
            messagebox.showwarning("Invalid Input", "Please enter a valid number.")

    # Create a new window for questions
    top = tk.Toplevel()
    top.configure(bg=BG_COLOR)
    top.title(f"{shape} Question")
    top.geometry("800x700")  # Increased size for the question window
    top.resizable(False, False)

    # Title
    tk.Label(top, text=f"Question about {shape}", font=("Arial", 20, "bold"), fg=HEADING_COLOR, bg=BG_COLOR).pack(pady=20)
    
    # Display the question
    tk.Label(top, text=question["q"], font=("Arial", 16), fg=TEXT_COLOR, bg=BG_COLOR).pack(pady=10)

    # Display image (same as in the lesson window)
    image_path = lesson["image"]
    img = tk.PhotoImage(file=image_path)
    image_label = tk.Label(top, image=img, bg=BG_COLOR)
    image_label.image = img  # keep a reference to the image
    image_label.pack(pady=10)

    # Input field for the answer
    answer_entry = tk.Entry(top, font=("Arial", 14), width=10)
    answer_entry.pack(pady=10)

    # Submit button
    submit_button = tk.Button(top, text="Submit", command=check_answer,
                              bg=BUTTON_COLOR, fg="white", font=("Arial", 12, "bold"),
                              padx=10, pady=5)
    submit_button.pack(pady=10)

    # Close button
    tk.Button(top, text="Close", command=top.destroy,
              bg=EXIT_BUTTON_COLOR, fg="white", font=("Arial", 12, "bold"),
              padx=10, pady=5).pack(pady=20)


def on_button_hover(button, color):
    """Change button color on hover."""
    button.bind("<Enter>", lambda event: button.config(bg=color))
    button.bind("<Leave>", lambda event: button.config(bg=BUTTON_COLOR))


def main_gui():
    root = tk.Tk()
    root.configure(bg=BG_COLOR)
    root.title("Intelligent Tutoring System")
    root.geometry("800x1000")  # Increased width and height to fit content better
    root.resizable(False, False)

    # Title
    tk.Label(root, text="📘 Intelligent Tutoring System", font=("Arial", 26, "bold"),
             fg=HEADING_COLOR, bg=BG_COLOR).pack(pady=20)
    tk.Label(root, text="Choose a shape to learn and practice!", font=("Arial", 18),
             fg=TEXT_COLOR, bg=BG_COLOR).pack(pady=10)

    for shape in lessons.keys():
        frame = tk.Frame(root, bg=BG_COLOR)
        frame.pack(pady=10)

        # Shape Lesson Button
        lesson_button = tk.Button(frame, text=f"📘 Learn {shape}",
                                  command=lambda s=shape: show_lesson(s),
                                  bg=BUTTON_COLOR, fg="white", font=("Arial", 14, "bold"),
                                  padx=20, pady=10, width=12)
        lesson_button.pack(side="left", padx=10)

        # Shape Question Button
        question_button = tk.Button(frame, text=f"📝 {shape} Quiz",
                                    command=lambda s=shape: ask_question(s),
                                    bg=BUTTON_COLOR, fg="white", font=("Arial", 14, "bold"),
                                    padx=20, pady=10, width=12)
        question_button.pack(side="left", padx=10)

        # Add hover effects
        on_button_hover(lesson_button, BUTTON_HOVER_COLOR)
        on_button_hover(question_button, BUTTON_HOVER_COLOR)

    tk.Button(root, text="Exit", command=root.destroy,
              bg=EXIT_BUTTON_COLOR, fg="white", font=("Arial", 14, "bold"),
              padx=10, pady=5).pack(pady=30)

    root.mainloop()