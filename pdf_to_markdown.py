import pdfplumber
import re
import argparse

def pdf_to_markdown(pdf_path, output_path):
    try:
        # 打开PDF文件
        with pdfplumber.open(pdf_path) as pdf:
            markdown_content = []
            
            # 遍历每一页
            for page in pdf.pages:
                # 提取文本
                text = page.extract_text()
                
                # 打印每页的内容以进行调试
                print(f"Page {page.page_number} content:\n{text}\n")
                
                # 基本的文本清理
                if text:
                    text = text.strip()
                    # 将连续的换行符替换为单个换行符
                    text = re.sub(r'\n\s*\n', '\n\n', text)
                    # 添加到markdown内容中
                    markdown_content.append(text)
            
            # 将所有内容组合成一个字符串
            final_content = '\n\n'.join(markdown_content)
            
            # 写入markdown文件
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(final_content)
            print(f'转换成功！Markdown文件已保存到: {output_path}')
    except Exception as e:
        print(f'转换过程中发生错误: {str(e)}')

def main():
    # 创建命令行参数解析器
    parser = argparse.ArgumentParser(description='将PDF转换为Markdown格式')
    parser.add_argument('input_pdf', help='输入PDF文件的路径')
    parser.add_argument('output_md', help='输出Markdown文件的路径')
    
    # 解析命令行参数
    args = parser.parse_args()
    
    # 执行转换
    pdf_to_markdown(args.input_pdf, args.output_md)

if __name__ == '__main__':
    main() 