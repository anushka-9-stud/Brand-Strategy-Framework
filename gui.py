# Author:Anushka Chintala
#This is the gui module for the brand strategy assistant code
#This program executes the code and displays output in the tkinter gui and then saves it into a csv file
import tkinter as tk
from tkinter import ttk, messagebox
from typing import List
from brandstrategy_code import BrandStrategyAssistant

class BrandStrategyGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Brand Strategy Assistant")
        self.root.geometry("800x600")
        
        # Initialising the brand strategy assistant
        self.assistant = BrandStrategyAssistant()
        
        # Create main frame
        self.main_frame = ttk.Frame(self.root, padding="10")
        self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Create input fields
        self.create_input_fields()
        
        # Create result display
        self.create_result_display()
        
        # Create buttons
        self.create_buttons()

    def create_input_fields(self):
        # Business Name
        ttk.Label(self.main_frame, text="Business Name:").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.business_name = ttk.Entry(self.main_frame, width=40)
        self.business_name.grid(row=0, column=1, columnspan=2, sticky=tk.W, pady=5)

        # Category
        ttk.Label(self.main_frame, text="Category:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.category = ttk.Combobox(self.main_frame, values=['food_beverage', 'personal_care', 'household'])
        self.category.grid(row=1, column=1, columnspan=2, sticky=tk.W, pady=5)
        self.category.set('food_beverage')

        # Price Point
        ttk.Label(self.main_frame, text="Price Point:").grid(row=2, column=0, sticky=tk.W, pady=5)
        self.price_point = ttk.Combobox(self.main_frame, values=['budget', 'mid-range', 'premium'])
        self.price_point.grid(row=2, column=1, columnspan=2, sticky=tk.W, pady=5)
        self.price_point.set('mid-range')

        # Budget Level
        ttk.Label(self.main_frame, text="Budget Level:").grid(row=3, column=0, sticky=tk.W, pady=5)
        self.budget_level = ttk.Combobox(self.main_frame, values=['low', 'medium', 'high'])
        self.budget_level.grid(row=3, column=1, columnspan=2, sticky=tk.W, pady=5)
        self.budget_level.set('medium')

        # Target Market
        ttk.Label(self.main_frame, text="Target Market:").grid(row=4, column=0, sticky=tk.W, pady=5)
        self.target_market = ttk.Frame(self.main_frame)
        self.target_market.grid(row=4, column=1, columnspan=2, sticky=tk.W, pady=5)

        # Create checkboxes for target market
        self.target_vars = {}
        target_options = (
            self.assistant.target_demographics['age_groups'] +
            self.assistant.target_demographics['lifestyles']
        )
        
        for i, option in enumerate(target_options):
            var = tk.BooleanVar()
            self.target_vars[option] = var
            cb = ttk.Checkbutton(self.target_market, text=option, variable=var)
            cb.grid(row=i//3, column=i%3, sticky=tk.W, padx=5)

    def create_result_display(self):
        # Create text widget for displaying results
        ttk.Label(self.main_frame, text="Strategy Results:").grid(row=10, column=0, sticky=tk.W, pady=5)
        self.result_text = tk.Text(self.main_frame, height=15, width=70)
        self.result_text.grid(row=11, column=0, columnspan=3, pady=5)
        
        # Add scrollbar
        scrollbar = ttk.Scrollbar(self.main_frame, orient=tk.VERTICAL, command=self.result_text.yview)
        scrollbar.grid(row=11, column=3, sticky=(tk.N, tk.S))
        self.result_text.configure(yscrollcommand=scrollbar.set)

    def create_buttons(self):
        button_frame = ttk.Frame(self.main_frame)
        button_frame.grid(row=12, column=0, columnspan=3, pady=10)
        
        ttk.Button(button_frame, text="Generate Strategy", command=self.generate_strategy).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Save to CSV", command=self.save_strategy).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Clear", command=self.clear_form).pack(side=tk.LEFT, padx=5)

    def get_selected_target_market(self) -> List[str]:
        return [k for k, v in self.target_vars.items() if v.get()]

    def generate_strategy(self):
        try:
            name = self.business_name.get()
            category = self.category.get()
            price_point = self.price_point.get()
            target_market = self.get_selected_target_market()
            
            if not name or not target_market:
                messagebox.showerror("Error", "Please fill in all required fields")
                return
            
            # Generate strategy components
            self.current_framework = self.assistant.generate_brand_framework(
                category, target_market, price_point
            )
            self.current_personality = self.assistant.suggest_brand_personality(
                target_market, price_point
            )
            self.current_campaign = self.assistant.create_marketing_campaign_outline(
                self.current_framework, self.budget_level.get()
            )
            
            # Display results
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, "Brand Strategy Analysis\n")
            self.result_text.insert(tk.END, "=" * 50 + "\n\n")
            
            # Business Name Analysis
            name_analysis = self.assistant.analyze_business_name(name)
            self.result_text.insert(tk.END, f"Business Name Analysis:\n")
            self.result_text.insert(tk.END, f"- Length: {name_analysis['length']}\n")
            self.result_text.insert(tk.END, f"- Memorable: {'Yes' if name_analysis['memorable'] else 'No'}\n\n")
            
            # Brand Framework
            self.result_text.insert(tk.END, "Brand Framework:\n")
            self.result_text.insert(tk.END, f"- Category: {self.current_framework['category']}\n")
            self.result_text.insert(tk.END, f"- Positioning: {self.current_framework['positioning']}\n")
            self.result_text.insert(tk.END, f"- Keywords: {', '.join(self.current_framework['keywords'])}\n\n")
            
            # Brand Personality
            self.result_text.insert(tk.END, "Brand Personality:\n")
            self.result_text.insert(tk.END, f"- Recommended: {', '.join(self.current_personality['recommended_personalities'])}\n")
            self.result_text.insert(tk.END, f"- Traits: {', '.join(self.current_personality['suggested_traits'])}\n\n")
            
            # Marketing Campaign
            self.result_text.insert(tk.END, "Marketing Campaign:\n")
            self.result_text.insert(tk.END, f"- Channels: {', '.join(self.current_campaign['recommended_channels'])}\n")
            self.result_text.insert(tk.END, f"- Duration: {self.current_campaign['campaign_duration']}\n")
            self.result_text.insert(tk.END, f"- Content Themes: {', '.join(self.current_campaign['content_themes'])}\n")
            self.result_text.insert(tk.END, f"- Key Messages:\n")
            for msg in self.current_campaign['key_messages']:
                self.result_text.insert(tk.END, f"  * {msg}\n")
            
        except Exception as e:
            messagebox.showerror("Error", f"Error generating strategy: {str(e)}")

    def save_strategy(self):
        try:
            if not hasattr(self, 'current_framework'):
                messagebox.showerror("Error", "Please generate a strategy first")
                return
                
            self.assistant.export_strategy(
                self.business_name.get(),
                self.current_framework,
                self.current_personality,
                self.current_campaign
            )
            messagebox.showinfo("Success", "Strategy saved successfully!")
            
        except Exception as e:
            messagebox.showerror("Error", f"Error saving strategy: {str(e)}")

    def clear_form(self):
        self.business_name.delete(0, tk.END)
        self.category.set('food_beverage')
        self.price_point.set('mid-range')
        self.budget_level.set('medium')
        for var in self.target_vars.values():
            var.set(False)
        self.result_text.delete(1.0, tk.END)

def main():
    root = tk.Tk()
    app = BrandStrategyGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
