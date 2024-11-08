import pdfplumber
import sys

def pdf_to_markdown(pdf_path, output_path):
    try:
        print(f'开始处理PDF文件: {pdf_path}')
        with pdfplumber.open(pdf_path) as pdf:
            markdown_content = []
            
            print(f'PDF总页数: {len(pdf.pages)}')
            for i, page in enumerate(pdf.pages, 1):
                print(f'正在处理第 {i} 页...')
                text = page.extract_text()
                
                if text:
                    # 基础清理
                    text = text.strip()
                    
                    # 只保留基本的换行，不做复杂处理
                    lines = text.splitlines()
                    cleaned_lines = [line.strip() for line in lines if line.strip()]
                    text = '\n\n'.join(cleaned_lines)
                    
                    markdown_content.append(text)
            
            # 简单合并所有页面内容
            final_content = '\n\n'.join(markdown_content)
            
            print(f'写入文件: {output_path}')
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(final_content)
            print(f'转换成功！Markdown文件已保存到: {output_path}')
    except Exception as e:
        print(f'转换过程中发生错误: {str(e)}')

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('使用方法: python pdf_to_markdown.py <输入PDF文件> <输出MD文件>')
        sys.exit(1)
    
    pdf_path = sys.argv[1]
    output_path = sys.argv[2]
    
    pdf_to_markdown(pdf_path, output_path) 