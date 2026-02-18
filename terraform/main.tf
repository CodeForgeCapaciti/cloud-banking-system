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

output "minio_volume_name" {
  value = docker_volume.minio_data.name
}

output "docker_network_name" {
  value = docker_network.banking_network.name
}

output "mongo_volume_name" {
  value = docker_volume.mongo_data.name
}