# DOCKERFILE TO LAUNCH THE MICRO-SERVICE

# Use an official Python runtime as a parent image
FROM python:3.8

# Set the working directory to /app
WORKDIR /app
RUN mkdir -p /app/api_rest

COPY api_rest/showcase /app/api_rest/showcase
COPY api_rest/*.py /app/api_rest/


##COPY /showcase/agilneva-fe/package.json /app/api_rest/showcase/agilneva-fe/package.json
COPY api_rest/showcase/agilneva-fe/dist /app/api_rest/showcase
#COPY api_rest/showcase/agilneva-fe/dist/assets /app/api_rest/showcase/assets

#COPY api_rest/showcase/agilneva-fe/dist/assets /app/api_rest/assets

#

# Make port 8000 available to the world outside this container
EXPOSE 5173

WORKDIR /app/api_rest/showcase

CMD ["python3", "-m", "http.server", "5173"]


