experiences = []


def add_experience(company, role, years):
    experience = {
        "company": company,
        "role": role,
        "years": years
    }

    experiences.append(experience)
    print("Experience added successfully.")


def display_experiences():
    print("User Experience:")

    for experience in experiences:
        print(
            f"{experience['role']} at "
            f"{experience['company']} - "
            f"{experience['years']} years"
        )


def main():
    add_experience("Tech Company", "Software Intern", 1)
    add_experience("Startup Inc.", "Developer", 2)

    display_experiences()


if __name__ == "__main__":
    main()