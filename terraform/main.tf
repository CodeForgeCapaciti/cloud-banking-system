terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0"
    }
  }
}

provider "docker" {}

resource "docker_network" "banking_network" {
  name = "banking_network"
}

resource "docker_volume" "mongo_data" {
  name = "mongo-data"
}

resource "docker_volume" "minio_data" {
  name = "minio-data"
}
