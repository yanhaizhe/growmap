import re

def extract_all_js_strings(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # We want to extract texts inside the script tag
    script_match = re.search(r'<script>(.*?)</script>', content, re.DOTALL)
    if not script_match:
        return []
    
    script_content = script_match.group(1)
    
    # Extract all string literals:
    # 1. Backticks
    backticks = re.findall(r'`(.*?)`', script_content, re.DOTALL)
    # 2. Single quotes (excluding small code strings and keys)
    single_quotes = re.findall(r"'(.*?)'", script_content, re.DOTALL)
    # 3. Double quotes
    double_quotes = re.findall(r'"(.*?)"', script_content, re.DOTALL)
    
    all_strings = backticks + single_quotes + double_quotes
    
    filtered_strings = []
    for s in all_strings:
        # Clean HTML tags and newlines
        clean = re.sub(r'<[^>]+>', ' ', s)
        clean = re.sub(r'\s+', ' ', clean).strip()
        # Keep only long strings containing Chinese characters (actual content, not code/selectors)
        if len(clean) > 20 and any('\u4e00' <= char <= '\u9fff' for char in clean):
            filtered_strings.append(clean)
            
    # Also get HTML body paragraphs
    body_content = content.split('<body>')[1].split('</body>')[0]
    p_tags = re.findall(r'<p[^>]*>(.*?)</p>', body_content, re.DOTALL)
    for p in p_tags:
        clean = re.sub(r'<[^>]+>', ' ', p)
        clean = re.sub(r'\s+', ' ', clean).strip()
        if len(clean) > 20:
            filtered_strings.append(clean)
            
    return list(set(filtered_strings))

def check_missing(interactive_texts, print_file_path):
    with open(print_file_path, 'r', encoding='utf-8') as f:
        print_content = f.read()
    print_content_clean = re.sub(r'<[^>]+>', ' ', print_content)
    print_content_clean = re.sub(r'\s+', ' ', print_content_clean)
    
    missing = []
    for text in interactive_texts:
        # Replace template literals variables
        query = re.sub(r'\$\{[^}]+\}', ' ', text)
        query = query.replace('小圆', '小睿睿')
        query = re.sub(r'\s+', ' ', query).strip()
        
        if len(query) < 15:
            continue
            
        # Take a signature
        sig = query[:15]
        if sig not in print_content_clean:
            found = False
            for i in range(0, len(query) - 15, 10):
                sub = query[i:i+15]
                if sub in print_content_clean:
                    found = True
                    break
            if not found:
                missing.append(text)
                
    return missing

if __name__ == '__main__':
    interactive_path = '/Users/yanhaizhe/Documents/同步空间/004-notespace/闫孜睿成长地图/小人书.html'
    print_path = '/Users/yanhaizhe/Documents/同步空间/004-notespace/闫孜睿成长地图/故事书打印版.html'
    
    texts = extract_all_js_strings(interactive_path)
    print(f"Extracted {len(texts)} unique text blocks from interactive version.")
    
    missing = check_missing(texts, print_path)
    print(f"Found {len(missing)} missing text blocks:")
    for m in missing:
        print(f"- {m[:120]}")
