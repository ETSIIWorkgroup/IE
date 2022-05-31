* Todos los nodos:
MATCH (n) RETURN n;

* Nodos que sean actores:
MATCH (n:Actor) RETURN n;

* Películas en las que ha participado un actor determinado:
MATCH (n:Actor{name:"Kevin Bacon"})-->(m:Movie) 
RETURN n.name, m.title;

* Películas en las que ha actuado un actor determinado:
MATCH (n:Actor{name:"Kevin Bacon"})-[:ACTED_IN]->(m:Movie) 
RETURN n.name, m.title;

* Directores que han dirigido a un actor determinado:
MATCH (n:Actor{name:"Kevin Bacon"})-[:ACTED_IN]->(m:Movie)<-[:DIRECTED]-(d:Director) 
RETURN n.name, m.title, d.name;

* Número de películas en las que ha actuado cada actor:
MATCH (n:Actor)-[:ACTED_IN]->(m:Movie) 
RETURN n.name, COUNT(m) AS works;

* Actor que ha participado en más películas:
MATCH (n:Actor)-[:ACTED_IN]->(m:Movie) 
RETURN n.name, COUNT(m) AS works
ORDER BY works DESC
LIMIT 1;

* Actores con un número de Bacon = 1:
MATCH (n:Actor{name:"Kevin Bacon"})-[:ACTED_IN]->(m:Movie)<-[:ACTED_IN]-(a:Actor) 
RETURN a.name, m.title;

* Valoraciones de usuarios a películas:
MATCH (u:User)-[r:RATED]->(m:Movie) 
RETURN u.name, m.title, r.rating;

* Top 10 de usuarios más participativos:
MATCH (u:User)-[r:RATED]->(:Movie) 
RETURN u.name, COUNT(r.rating) AS reviews 
ORDER BY reviews DESC 
LIMIT 10;

* Buscar la película de "La vida de Brian" (uso de expresiones regulares):
MATCH (m:Movie) 
WHERE m.title =~ '.*Brian.*' 
RETURN m.title;

* Películas valoradas por el usuario "Mr. Jason Love":
MATCH (u:User{name:"Mr. Jason Love"})-[r:RATED]-> (m:Movie) 
RETURN u.name, m.title, r.rating;

* Películas mejor valoradas por el usuario "Mr. Jason Love":
MATCH (u:User{name:"Mr. Jason Love"})-[r:RATED]-> (m:Movie) 
RETURN u.name, m.title, r.rating 
ORDER BY r.rating DESC;

* Usuarios que han valorado con 5 estrellas las mismas películas que "Mr. Jason Love":
MATCH (u:User{name:"Mr. Jason Love"})-[:RATED {rating:5.0}]-> (m:Movie)<-[:RATED {rating:5.0}]-(bro:User)
RETURN u.name, bro.name, m.title;

* Usuarios con gustos similares a los de "Mr. Jason Love":
	- Usuarios que han valorado de forma parecida alguna pelí­cula:
MATCH (u:User{name:"Mr. Jason Love"})-[r1:RATED]-> (m:Movie)<-[r2:RATED]-(bro:User)
WHERE ABS(r1.rating - r2.rating) <= 1
RETURN u.name, bro.name, m.title, ABS(r1.rating - r2.rating) AS divergence;

* Actores que han participado en "La vida de Brian":
MATCH (a:Actor)-[:ACTED_IN]->(m:Movie)
WHERE m.title =~ '.*Life.*Brian.*'
RETURN a.name

* bla bla bla
MATCH (u:User)-[r:RATED]->(m:Movie) WITH u, MAX(r.rating) AS max_rating MATCH (u)-[r:RATED{rating:max_rating}]->(m:Movie) RETURN u.name, m.title, r.rating;

* bla bla bla
MATCH (u:User{name:"Mr. Jason Love"})-[r1.RATED]->(m.Movie)<-[r2.RATED]-(bro:User) WHERE ABS(r1.rating - r2.rating) <= 1 RETURN m.title, bro.name, ABS(r1.rating - r2.rating) AS divergence ORDER BY divergence ASC;

* Actores favoritos de los usuarios(Mr. Jason)
MATCH (u:User{name:"Mr. Jason Love"})-[r:RATED]->(m:Movie)<-[:ACTED_IN]-(a:Actor) WHERE r.rating > 3 RETURN a.name, COUNT(m) AS likes, SUM(r.rating) AS ratings ORDER BY ratings, likes DESC;

* El género más seguido
/// <>  significa "distinto de"
MATCH (k:Actor{name:"Kevin Bacon"})-[:ACTED_IN]->(:Movie)<-[:ACTED_IN]-(a:Actor)
MATCH (a) -[:ACTED_IN]->(:Movie)<-[:ACTED_IN]-(b:Actor)
WHERE b<>k AND NOT (k)-[:ACTED_IN]->(:Movie)<- [:ACTED_IN]-(b:Actor) RETURN b.name;

// Cargar un CSV; un atributo por cada cabecera del fichero
LOAD CSV WITH HEADERS FROM "file:///characters.csv" AS line CREATE (:Characters{name:line.name, height:line.height, mass:line.mass, hair_color:line.hair_color, skin_color:line.skin_color, eye_color:line.eye_color, birth_year:line.birth_year, gender:line.gender, homeworld:line.homeworld, species:line.species})

LOAD CSV WITH HEADERS FROM "file:///planets.csv" AS line CREATE (:Planets{name:line.name, rotation_period:line.rotation_period, orbital_period:line.orbital_period, diameter:line.diameter, climate:line.climate, gravity:line.gravity, terrain:line.terrain, surface_water:line.surface_water, population:line.population}) 

LOAD CSV WITH HEADERS FROM "file:///species.csv" AS line CREATE (:Species{name:line.name, classification:line.classification, designation:line.designation, average_height:line.average_height, skin_colors:line.skin_colors, hair_colors:line.hair_colors, eye_colors:line.eye_colors, average_lifespan:line.average_lifespan, language:line.language, homeworld:line.homeworld}) 

MATCH(n) RETURN n;

// ESTO SOLO FUNCIONA CON NODOS SIN ARISTAS!
MATCH(n) DELETE n; 

// ESTO SE CARGA TODOS LOS NODOS INCLUSO CON ARISTAS!
MATCH(n) DETACH DELETE n;

// Arista entre personajes y sus planetas de origen; la arista se llama WAS_BORN_IN y contiene una 
// propiedad que representa la fecha de nacimiento.
MATCH (n:Characters), (m:Planets) WHERE n.homeworld = m.name CREATE (n)-[:WAS_BORN_IN{birth:n.birth_year}]->(m);

// Arista entre personajes y la especie a la que pertenecen. Sin atributo especificado.
MATCH (n:Characters), (m:Species) WHERE n.species = m.name CREATE (n)-[:BELONGS_TO_SPECIES]->(m);

// Especie más numerosa
MATCH (n:Characters)-[r:BELONGS_TO_SPECIES]->(s:Species) RETURN s.name, COUNT(r) AS poblacion ORDER BY poblacion DESC LIMIT 1;

// Personajes sin origen conocido
MATCH(c:Characters)->(:Planets{name:"NA"}) RETURN c.name

//Crear una relación :LE_GUSTA entre un Usuario y una película si un
//Usuario ha valorado una Película con 4 ó 5 estrellas
MATCH (a:User)-[r:RATED]->(m:Movie) WHERE r.rating = 4 OR r.rating = 5 CREATE (a)-[:LIKES]->(m);

//Crear una relación :PARECIDOS entre dos Usuarios si coinciden en
//que les gustan más de X Películas (fijar un umbral)
MATCH (u:User)-[:LIKES]->(m:Movie)<-[:LIKES]-(bro:User) WITH u,bro, COUNT(m) AS coincidencias WHERE coincidencias >=19 MERGE (u)-[:PARECIDO]->(bro);

// Versión del profesor:
MATCH (u:User)-[:LIKES]->(m:Movie)<-[:LIKES]-(bro:User) WITH u,bro, COUNT(m) AS coincidencias
WHERE u1<> bro AND coincidencias>20 
MERGE (u)-[:PARECIDO]->(bro);

//Recomendar a un usuario las películas que les gustan a sus usuarios parecidos:
MATCH (u:User{name:"Mr. Jason Love"})-[:PARECIDO]->(u:User)-[r:LIKES]->(m:Movie)
WHERE NOT (u)-[:RATED]->(m)
RETURN u.name, m.title;