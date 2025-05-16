
# airflow-pet-project

A hands-on demonstration of orchestrating data pipelines using **Apache Airflow**, **dbt (data build tool)**, and **data contracts** to ensure data quality and reliability.

## 🚀 Project Overview

This project showcases how to:

- Utilize **Apache Airflow** for scheduling and orchestrating data workflows.
- Implement **dbt** for transforming data within your warehouse.
- Enforce **data contracts** to maintain schema consistency and data quality.

By integrating these tools, you can build robust, scalable, and maintainable data pipelines.

## 📁 Repository Structure

```
.
├── .dbt/                    # dbt project directory
│   ├── models/             # dbt models
│   ├── seeds/              # dbt schemas
│   ├── dbt_project.yml     # dbt project configuration
│   └── profiles.yml        # dbt profiles for connection settings
├── dags/                   # Airflow DAG definitions
├── data/                   # JSON data folder to upload into PostgreSQL
├── docker-compose.yaml     # Docker Compose setup for Airflow and dbt
├── Dockerfile              # Dockerfile for custom image builds
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

## 🛠️ Setup Instructions

### Prerequisites

- [Docker](https://www.docker.com/get-started) and [Docker Compose](https://docs.docker.com/compose/install/) installed on your machine.
- Basic understanding of Python and SQL.

### Clone the Repository

```bash
git clone https://github.com/Shiqarno/airflow-pet-project.git
cd airflow-pet-project
```

### Build and Start the Services

```bash
docker-compose up -d
```

This command will:

- Build the Docker images for Airflow with dbt.
- Start the Airflow webserver, scheduler, and metadata database.

### Access Airflow UI

Once the services are up and running, access the Airflow web interface at:

[http://localhost:8080](http://localhost:8080)

Use the default credentials:

- **Username:** `airflow`
- **Password:** `airflow`

## 📝 License

This project is licensed under the [MIT License](LICENSE).
