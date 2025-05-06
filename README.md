# Spelling_Corrector_NLP

A Python-based **spelling correction system** that uses probabilistic models, edit distance algorithms, and customizable corpus data to detect and correct misspelled words. Comes with both a **Tkinter GUI** and a **Streamlit web interface**.

---

## 🚀 Features

✅ Detects and corrects misspelled words  
✅ Suggests the most likely intended correction  
✅ Handles typos, character swaps, and similar keyboard errors  
✅ Uses **edit distance (Levenshtein)** and **word probabilities** for correction  
✅ Supports both **single-word** and **sentence-level** correction  
✅ Built-in **Tkinter desktop GUI**  
✅ **Streamlit app** for browser-based interaction  
✅ Easy to extend with custom corpus or vocabulary

---

## 🏗️ **How It Works**

The system:  
1. Loads a **corpus file** (default: `data/big.txt`) to build a word frequency dictionary  
2. Uses **edit distance (1 and 2 edits away)** to generate candidate corrections  
3. Ranks candidates based on **Laplace-smoothed word probabilities** and **Levenshtein distance**  
4. Applies correction **word-by-word** on user input  

---

## 📂 **Project Structure**
```
├── data/
│   └── big.txt               # Corpus file
├── spelling_corrector.py      # Core spelling correction logic
├── gui.py                     # Tkinter desktop GUI
├── app.py                     # Streamlit web app
├── README.md
└── requirements.txt           # Required Python packages
```
## 📝 **Example Usage (Python)**

```python
from spelling_corrector import SpellingCorrector

corrector = SpellingCorrector('data/big.txt')

text = "I recieved teh letter adn it was amazng"
corrected = corrector.correct_text(text)

print("Original:", text)
print("Corrected:", corrected)
```
## **📦 Installation**
```
git clone https://github.com/ArhamMahmood/Spelling_Corrector_NLP.git
cd Spelling_Corrector_NLP
pip install -r requirements.txt
```
