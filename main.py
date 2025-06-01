def remove_subdomains(input_file=None, output_file=None, allowed_extensions=None):
    default_extensions = {'.go.id', '.ac.id', '.sch.id', '.co.id', '.ponpes.id', '.desa.id'}
    allowed_extensions = allowed_extensions or default_extensions
    domains = set()

    if not input_file:
        input_file = input("Masukkan nama file input: ").strip()
    if not output_file:
        output_file = input("Masukkan nama file output: ").strip()

    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            for line in f:
                domain = line.strip().lower()
                if not domain:
                    continue
                if any(domain.endswith(ext) for ext in allowed_extensions):
                    domains.add(domain)
    except FileNotFoundError:
        print(f"Error: File '{input_file}' tidak ditemukan.")
        return
    except PermissionError:
        print(f"Error: Tidak ada izin untuk membaca file '{input_file}'.")
        return
    except UnicodeDecodeError:
        print(f"Error: Tidak dapat mendekode file '{input_file}'. Pastikan file menggunakan encoding UTF-8.")
        return
    except Exception as e:
        print(f"Error tak terduga saat membaca file '{input_file}': {str(e)}")
        return

    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            for domain in sorted(domains):
                f.write(f"{domain}\n")
        print(f"Domain dengan ekstensi yang diizinkan telah disimpan di '{output_file}'")
        print(f"Jumlah domain yang disimpan: {len(domains)}")
    except PermissionError:
        print(f"Error: Tidak ada izin untuk menulis ke file '{output_file}'.")
    except Exception as e:
        print(f"Error tak terduga saat menulis ke file '{output_file}': {str(e)}")

def main():
    remove_subdomains()

if __name__ == "__main__":
    main()
