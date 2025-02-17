from django.shortcuts import render,HttpResponse
from django.shortcuts import render


# Create your views here.
def home(request):
    data = {
        #this section contains my personals details and social media urls
        "name": "Rachit Mehul Pathak",
        "email": "rmp10015@nyu.edu",
        "phone": "+1 (551) 371-2428",
        "linkedin": "https://www.linkedin.com/in/rachit-pathak-65b676230/",
        "github": "https://github.com/rachitt",

        #This part contains my educational details
        "education": {
            "masters": {
                "degree": "M.S. in Computer Science",
                "institution": "New York University – Tandon School of Engineering",
                "year": "Exp. May 2026"
            },
            "bachelors": {
                "degree": "B.Tech. in Computer Science (AI & Robotics)",
                "institution": "Vellore Institute of Technology",
                "year": "May 2024"
            }
        },

        #this part contains my skills
        "skills": {
            "programming": "Python, SQL, JavaScript, MATLAB, CSS, HTML, XML",
            "frameworks": "AWS, Docker, Apache Spark, TensorFlow, Node.js, Express.js, Git, Hadoop, Streamlit",
            "databases": "Kubernetes, DynamoDB, MySQL, MongoDB"
        },

        #This part contains my work ex
        "experience": [
            {
                "role": "Machine Learning Engineer Intern",
                "company": "EssentiallySports, New Delhi",
                "duration": "Jan 2024 – Jun 2024",
                "responsibilities": [
                    "Developed AI-driven solutions for sports journalism.",
                    "Led an advanced article recommendation engine using ML techniques."
                ]
            },
            {
                "role": "Deep Learning Engineer Intern",
                "company": "ResoluteAI Software, Bengaluru",
                "duration": "Jun 2023 – Sept 2023",
                "responsibilities": [
                    "Trained object detection models (ResNet-50, YOLOv5).",
                    "Led a team of 4 interns on a glass manufacturing project, improving accuracy by 15%."
                ]
            },
            {
                "role": "Software Developer Engineer Intern",
                "company": "Cephas Consultancy Services Private Ltd., Bengaluru",
                "duration": "May 2022 – Sept 2022",
                "responsibilities": [
                    "Created XML feeds and built job listings using WordPress."
                ]
            }
        ],

        #this part contains my academic projects
        "projects": [
            {
                "title": "Optimizing Gameplay: RL Algorithms on 2048 Tiles Problem",
                "year": "NYU - Fall 2024",
                "details": [
                    "Implemented RL models (Q-Learning, DQN, MCTS) for optimizing gameplay.",
                    "Analyzed performance using episode length, training time, and rewards."
                ]
            },
            {
                "title": "e-Waste Segregation and Management Capstone Project",
                "year": "VIT - Spring 2024",
                "details": [
                    "Created a dataset of 5000+ images for waste classification.",
                    "Submitted a research paper to ScienceDirect Journal."
                ]
            },
            {
                "title": "Learning Model for Autistic and Dyslexic Children",
                "year": "VIT - Spring 2023",
                "details": [
                    "Tailored a personalized learning model for children with disabilities, integrating VGG-16 and InceptionV4 for visual cue analysis.",
                    "Study published in International Journal “Innovative Research Thoughts”."
                ]
            },
            {
                "title": "Super Predictor for Indian Premier League",
                "year": "VIT - Fall 2022",
                "details": [
                    "Applied Naïve Bayes, Random Forest and K-Means Clustering to predict outcome of a game in IPL.",
                    "Study published in International Journal “Innovative Research Thoughts”."
                ]
            },
        ],
        #My awards and leadership experiences
        "awards": [
            "Special mention at VITCC-Intra MUN 2022 in Security Council Committee.",
            "Coordinated programming department of ASTREx at VIT Chennai."
        ]
    }
    return render(request, "index.html", {"cv": data})