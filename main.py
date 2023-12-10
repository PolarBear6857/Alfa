from itertools import permutations

subjects = [
    ("Český jazyk", "ČJ"),
    ("Angličtina", "A"),
    ("Matematika", "M"),
    ("Tělocvik", "TV"),
    ("Programové vybavení", "PV"),
    ("Databázové systémy", "DS"),
    ("Podnikové informační systémy", "PIS"),
    ("Počítačové systémy a sítě", "PSS"),
    ("Aplikovaná matematika", "AM"),
    ("Cvičení ze správy IT", "CIT"),
    ("Webové aplikace", "WA"),
    ("Technický projekt", "TP"),
]


# Function to generate schedule variants
def generate_schedule_variants(subjects, limit=100):
    subject_permutations = permutations(subjects)

    count = 0
    for perm in subject_permutations:
        schedule = []
        day_hours = 0

        for subject in perm:
            if day_hours + subject_hours[subject[1]] <= 10:
                schedule.append(subject)
                day_hours += subject_hours[subject[1]]

                if day_hours == 10:
                    day_hours = 0
            else:
                day_hours = subject_hours[subject[1]]
                schedule.append(subject)

        if 4 <= len(schedule) <= 10:
            yield schedule
            count += 1

            # Print the generated schedule variant
            print(f"Generated Schedule Variant #{count}: {schedule}")

        if count == limit:
            break


subject_hours = {
    "ČJ": 4,
    "A": 5,
    "M": 4,
    "TV": 2,
    "PV": 3,
    "DS": 3,
    "PIS": 4,
    "PSS": 3,
    "AM": 2,
    "CIT": 2,
    "WA": 3,
    "TP": 1,
}

print("Generating...\n")

variants_generator = generate_schedule_variants(subjects, limit=1)

for variant in variants_generator:
    print(variant)

print("Done!\n")
