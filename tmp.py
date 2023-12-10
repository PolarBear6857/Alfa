import random

subjects = [
    ("Český jazyk", "ČJ", 3),
    ("Angličtina", "A", 4),
    ("Matematika", "M", 4),
    ("Tělocvik", "TV", 2),
    ("Programové vybavení", "PV", 3),
    ("Databázové systémy", "DS", 3),
    ("Podnikové informační systémy", "PIS", 4),
    ("Počítačové systémy a sítě", "PSS", 3),
    ("Aplikovaná matematika", "AM", 2),
    ("Cvičení ze správy IT", "CIT", 2),
    ("Webové aplikace", "WA", 3),
    ("Technický projekt", "TP", 1),
]

teachers = ["Teacher1", "Teacher2", "Teacher3", "Teacher4", "Teacher5"]
classrooms = [101, 102, 103, 104, 105]


def generate_timetable(subjects, teachers, classrooms, week_days=5, min_lessons_per_week=5, max_lessons_per_day=10,
                       max_lunch_breaks_per_week=2):
    # Validate input constraints
    if min_lessons_per_week < week_days or max_lessons_per_day * week_days < min_lessons_per_week:
        raise ValueError("Invalid input constraints")

    timetable = {day: [] for day in range(1, week_days + 1)}
    available_slots = week_days * max_lessons_per_day
    lunch_breaks = 0

    # Generate a random number of lessons for each subject
    lessons_per_subject = {subject_code: frequency for _, subject_code, frequency in subjects}
    total_lessons = sum(lessons_per_subject.values())

    # Validate that the total number of lessons can fit in the timetable
    if total_lessons > available_slots:
        raise ValueError("Total number of lessons exceeds available slots in the timetable")

    # Generate timetable with constraints
    while total_lessons > 0 and available_slots > 0:
        # Choose a subject with remaining frequency
        subject_name, subject_code, frequency = random.choice(subjects)
        if (
                lessons_per_subject[subject_code] > 0
                and frequency > 0
        ):
            # Choose a day with available space
            day = random.randint(1, week_days)
            while len(timetable[day]) >= max_lessons_per_day or (
                    len(timetable[day]) >= min_lessons_per_week and timetable[day][-1] == "None"
            ):
                day = random.randint(1, week_days)

            # Choose a teacher and classroom
            teacher = random.choice(teachers)
            classroom = random.choice(classrooms)

            # Add the lesson to the timetable
            timetable[day].append((subject_code, teacher, classroom))
            lessons_per_subject[subject_code] -= 1
            total_lessons -= 1
            available_slots -= 1

            # Handle lunch breaks
            if lunch_breaks < max_lunch_breaks_per_week and random.random() < 0.2:  # 20% chance for lunch break
                timetable[day].append("None")
                available_slots -= 1
                lunch_breaks += 1

            # Handle additional conditions
            frequency -= 1

    # Convert timetable to a hashable format (tuple) for set storage
    timetable_tuples = tuple(sorted((day, tuple(timetable[day])) for day in timetable))

    return timetable_tuples


def print_timetable_set(timetable_set):
    for i, timetable in enumerate(timetable_set, start=1):
        print(f"Timetable {i}:")
        for day, day_timetable in timetable:
            formatted_timetable = []
            for item in day_timetable:
                if isinstance(item, tuple):
                    subject_code, teacher, classroom = item
                    formatted_timetable.append(f"[{subject_code}, {teacher}, {classroom}]")
                else:
                    formatted_timetable.append("[Přestávka]")
            print(f"[Day {day}-timetable]")
            print(" ".join(formatted_timetable))
        print()


vice_rozvrhu = set()
while len(vice_rozvrhu) < 1000:
    vice_rozvrhu.add(generate_timetable(subjects, teachers, classrooms))

print("Generated Timetable Set:")
print_timetable_set(vice_rozvrhu)
