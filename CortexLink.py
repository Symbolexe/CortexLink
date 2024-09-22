import argparse
from googlesearch import search
from time import sleep
from tabulate import tabulate
from colorama import Fore, init
init(autoreset=True)
def perform_search(query, num_results=10, region=None, lang="en", output_file="Cortex-Link-Result.txt",
                   use_table=False, no_color=False, proxy=None, ssl_verify=True, sleep_interval=0):
    try:
        with open(output_file, 'w') as output:
            results = []
            print(f"[*] Fetching results for '{query}'...")
            search_results = search(query, num_results=num_results, region=region, lang=lang, 
                                    proxy=proxy, ssl_verify=ssl_verify, sleep_interval=sleep_interval)
            for result in search_results:
                results.append(result)
                output.write(result + "\n")
                if not use_table:
                    if not no_color:
                        print(Fore.GREEN + result)
                    else:
                        print(result)
            if use_table:
                headers = ["No", "URL"]
                table_data = [[i + 1, res] for i, res in enumerate(results)]
                print(tabulate(table_data, headers=headers, tablefmt="grid"))
            print(f"\n[+] Results have been saved to {output_file}")
    except Exception as e:
        print(f"[!] An error occurred: {e}")
def main():
    parser = argparse.ArgumentParser(description="CortexLink Search Tool")
    parser.add_argument('-query', required=True, type=str, help='The search query you want to perform')
    parser.add_argument('-region', required=False, type=str, help='The region for search results (e.g., us, uk, fr)')
    parser.add_argument('-lang', default="en", type=str, help='Language for search results (default: en)')
    parser.add_argument('-n', '--num_results', type=int, default=10, help='Number of search results to return (default: 10)')
    parser.add_argument('-o', '--output', type=str, default="Cortex-Link-Result.txt", help='The output file to save results (default: Cortex-Link-Result.txt)')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-cve', action='store_true', help='Search for CVE Links')
    group.add_argument('-exploit', action='store_true', help='Search for Exploit Links')
    group.add_argument('-poc', action='store_true', help='Search for PoC Links')
    group.add_argument('-learn', action='store_true', help='Search for Learning and Education Links')
    parser.add_argument('--table', action='store_true', help='Display results in table format in the terminal')
    parser.add_argument('--no-color', action='store_true', help='Disable colored output')
    parser.add_argument('--proxy', type=str, help='Use a single proxy (format: http://user:pass@host:port)')
    parser.add_argument('--ssl_verify', action='store_false', help='Disable SSL verification for proxy connections')
    parser.add_argument('--sleep_interval', type=int, default=0, help='Time to wait between requests (default: 0 seconds)')
    args = parser.parse_args()
    if args.cve:
        final_query = f"{args.query} CVE list"
    elif args.exploit:
        final_query = f"{args.query} exploits download"
    elif args.poc:
        final_query = f"{args.query} PoC download"
    elif args.learn:
        final_query = f"{args.query} crash course"
    else:
        print("[!] No valid search option selected.")
        return
    perform_search(
        query=final_query,
        num_results=args.num_results,
        region=args.region,
        lang=args.lang,
        output_file=args.output,
        use_table=args.table,
        no_color=args.no_color,
        proxy=args.proxy,
        ssl_verify=args.ssl_verify,
        sleep_interval=args.sleep_interval
    )
if __name__ == "__main__":
    main()
