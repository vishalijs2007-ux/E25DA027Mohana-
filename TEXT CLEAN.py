import string

# Define a small set of common stopwords
STOPWORDS = {"a", "an", "the", "and", "or", "is", "in", "to", "with", "my", "of"}

# --- Basic cleaning ---
def basic_clean(text):
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    return text

# --- Remove stopwords ---
def remove_stopwords(text):
    words = text.split()
    filtered = [word for word in words if word not in STOPWORDS]
    return " ".join(filtered)

# --- Simple normalization (basic suffix removal for demonstration) ---
def normalize_text(text):
    words = text.split()
    normalized = [word.rstrip('ing') if word.endswith('ing') else word for word in words]
    return " ".join(normalized)

# --- Main cleaning pipeline for a single string ---
def clean_text(text, remove_stopwords_flag=True, normalize_flag=True):
    text = basic_clean(text)
    if remove_stopwords_flag:
        text = remove_stopwords(text)
    if normalize_flag:
        text = normalize_text(text)
    return text

# --- Cleaning pipeline for a list of sentences ---
def clean_text_list(sentences, remove_stopwords_flag=True, normalize_flag=True):
    return [clean_text(sentence, remove_stopwords_flag, normalize_flag) for sentence in sentences]

# --- Example ---
dataset = [
    "I love my cats!",
    "Running to the park with my dog.",
    "The weather is amazing today."
]

cleaned_dataset = clean_text_list(dataset)
print(cleaned_dataset)
