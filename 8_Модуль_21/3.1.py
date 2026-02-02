import re
from typing import List, Dict, Set
from dataclasses import dataclass
from pathlib import Path
import argparse


@dataclass
class Contact:
    """Класс для хранения данных контакта."""
    full_name: str = ""
    phone_numbers: List[str] = None
    email: str = ""
    organization: str = ""
    title: str = ""
    note: str = ""

    def __post_init__(self):
        if self.phone_numbers is None:
            self.phone_numbers = []

    def get_primary_phone(self) -> str:
        """Возвращает первый номер телефона или пустую строку."""
        return self.phone_numbers[0] if self.phone_numbers else ""

    def to_vcf(self) -> str:
        """Преобразует контакт в формат vCard."""
        vcf_lines = ["BEGIN:VCARD", "VERSION:3.0"]

        # Имя
        if self.full_name:
            vcf_lines.append(f"FN:{self.full_name}")
            # Пробуем разобрать имя на компоненты
            parts = self.full_name.split()
            if len(parts) >= 2:
                given = parts[0]
                family = parts[-1]
                middle = ' '.join(parts[1:-1]) if len(parts) > 2 else ""
                vcf_lines.append(f"N:{family};{given};{middle};;")

        # Телефоны
        for i, phone in enumerate(self.phone_numbers):
            phone_clean = re.sub(r'\D', '', phone)
            type_label = "TYPE=CELL" if i == 0 else "TYPE=HOME"
            vcf_lines.append(f"TEL;{type_label}:{phone}")

        # Email
        if self.email:
            vcf_lines.append(f"EMAIL:{self.email}")

        # Организация и должность
        if self.organization or self.title:
            org_line = f"ORG:{self.organization}"
            if self.title:
                org_line += f";{self.title}"
            vcf_lines.append(org_line)

        # Заметка
        if self.note:
            # VCF требует экранирования переносов строк
            note_escaped = self.note.replace('\n', '\\n')
            vcf_lines.append(f"NOTE:{note_escaped}")

        vcf_lines.append("END:VCARD")
        return '\n'.join(vcf_lines)


class PhoneBookCleaner:
    """Класс для очистки телефонного справочника от дубликатов."""

    def __init__(self):
        self.contacts_by_phone: Dict[str, Contact] = {}
        self.duplicates_count = 0

    def parse_vcf(self, file_path: str) -> List[Contact]:
        """Парсит VCF файл и возвращает список контактов."""
        contacts = []
        current_contact = None
        current_phone_numbers = []

        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()
        except UnicodeDecodeError:
            with open(file_path, 'r', encoding='cp1251') as f:
                lines = f.readlines()

        for line in lines:
            line = line.strip()

            if line == "BEGIN:VCARD":
                current_contact = Contact()
                current_phone_numbers = []

            elif line.startswith("FN:"):
                if current_contact:
                    current_contact.full_name = line[3:]

            elif line.startswith("TEL;"):
                # Извлекаем номер телефона (после последнего ':')
                phone = line.split(':')[-1]
                if phone:
                    current_phone_numbers.append(phone)

            elif line.startswith("EMAIL:"):
                if current_contact:
                    current_contact.email = line[6:]

            elif line.startswith("ORG:"):
                if current_contact:
                    org_parts = line[4:].split(';')
                    current_contact.organization = org_parts[0]
                    if len(org_parts) > 1:
                        current_contact.title = org_parts[1]

            elif line.startswith("NOTE:"):
                if current_contact:
                    note = line[5:].replace('\\n', '\n')
                    current_contact.note = note

            elif line == "END:VCARD":
                if current_contact and current_phone_numbers:
                    current_contact.phone_numbers = current_phone_numbers
                    contacts.append(current_contact)
                current_contact = None

        return contacts

    def normalize_phone(self, phone: str) -> str:
        """Нормализует номер телефона для сравнения."""
        # Удаляем все нецифровые символы
        digits = re.sub(r'\D', '', phone)

        # Обрабатываем российские номера
        if digits.startswith('8') and len(digits) == 11:
            digits = '7' + digits[1:]  # Заменяем 8 на 7
        elif digits.startswith('+7') and len(digits) == 12:
            digits = digits[1:]  # Убираем +

        return digits

    def remove_duplicates(self, contacts: List[Contact]) -> List[Contact]:
        """Удаляет дубликаты контактов по номеру телефона."""
        unique_contacts = []
        seen_phones: Set[str] = set()
        self.duplicates_count = 0

        for contact in contacts:
            if not contact.phone_numbers:
                # Контакты без телефонов добавляем как есть
                unique_contacts.append(contact)
                continue

            is_duplicate = False
            for phone in contact.phone_numbers:
                normalized = self.normalize_phone(phone)
                if normalized in seen_phones:
                    is_duplicate = True
                    self.duplicates_count += 1
                    print(f"Дубликат найден: {contact.full_name} - {phone}")
                    break

            if not is_duplicate:
                unique_contacts.append(contact)
                for phone in contact.phone_numbers:
                    normalized = self.normalize_phone(phone)
                    seen_phones.add(normalized)

        return unique_contacts

    def save_to_vcf(self, contacts: List[Contact], output_path: str):
        """Сохраняет контакты в VCF файл."""
        with open(output_path, 'w', encoding='utf-8') as f:
            for contact in contacts:
                f.write(contact.to_vcf() + '\n\n')

    def process_file(self, input_file: str, output_file: str = None):
        """Основной метод обработки файла."""
        if not output_file:
            input_path = Path(input_file)
            output_file = input_path.parent / f"cleaned_{input_path.name}"

        print(f"Чтение файла: {input_file}")
        contacts = self.parse_vcf(input_file)
        print(f"Найдено контактов: {len(contacts)}")

        print("\nПоиск дубликатов...")
        unique_contacts = self.remove_duplicates(contacts)

        print(f"\nДубликатов найдено: {self.duplicates_count}")
        print(f"Уникальных контактов осталось: {len(unique_contacts)}")

        self.save_to_vcf(unique_contacts, output_file)
        print(f"\nРезультат сохранен в: {output_file}")

        return unique_contacts


def create_sample_vcf():
    """Создает тестовый VCF файл с дубликатами."""
    sample_content = """BEGIN:VCARD
VERSION:3.0
FN:Иван Иванов
TEL;TYPE=CELL:+79161234567
EMAIL:ivan@mail.ru
ORG:Компания А
TITLE:Менеджер
END:VCARD

BEGIN:VCARD
VERSION:3.0
FN:Петр Петров
TEL;TYPE=CELL:+7 (916) 123-45-67
EMAIL:peter@gmail.com
ORG:Компания Б
END:VCARD

BEGIN:VCARD
VERSION:3.0
FN:Мария Сидорова
TEL;TYPE=CELL:89167778899
EMAIL:maria@ya.ru
END:VCARD

BEGIN:VCARD
VERSION:3.0
FN:Сергей Сергеев
TEL;TYPE=CELL:8 (916) 777-88-99
EMAIL:sergey@mail.ru
END:VCARD

BEGIN:VCARD
VERSION:3.0
FN:Анна Аннова
TEL;TYPE=CELL:+79160001122
END:VCARD"""

    with open("sample_contacts.vcf", "w", encoding="utf-8") as f:
        f.write(sample_content)
    print("Создан тестовый файл: sample_contacts.vcf")


def main():
    """Основная функция программы."""
    parser = argparse.ArgumentParser(description='Удаление дубликатов контактов по номеру телефона')
    parser.add_argument('input', nargs='?', help='Входной VCF файл')
    parser.add_argument('-o', '--output', help='Выходной VCF файл')
    parser.add_argument('--create-sample', action='store_true',
                        help='Создать тестовый VCF файл с дубликатами')

    args = parser.parse_args()

    if args.create_sample:
        create_sample_vcf()
        return

    if not args.input:
        parser.print_help()

        # Интерактивный режим
        choice = input("\nХотите создать тестовый файл? (y/n): ").lower()
        if choice == 'y':
            create_sample_vcf()
            input_file = "sample_contacts.vcf"
            output_file = "cleaned_contacts.vcf"

            cleaner = PhoneBookCleaner()
            cleaner.process_file(input_file, output_file)
        return

    # Обработка указанного файла
    cleaner = PhoneBookCleaner()
    cleaner.process_file(args.input, args.output)


if __name__ == "__main__":
    main()