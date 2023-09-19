            var myHeaders = new Headers();
            myHeaders.append("accept", "application/json");
    
            var requestOptions = {
                method: 'GET',
                headers: myHeaders,
                redirect: 'follow'
            };
            function get_data() {
                fetch('https://techlabs-demo-evently.onrender.com/event/')
                  .then(response => response.json())
                  .then(data => {
                    data.forEach(function(item) {
                      let sectionId;
                      switch(item.objektart) {
                        case "MuseumSonstiges":
                          sectionId = "#o-museums";
                          break;
                        case "Heimatkundemuseum":
                          sectionId = "#l-museums";
                          break;
                        case "Technikmuseum":
                          sectionId = "#t-museums";
                          break;
                        case "Naturkundemuseum":
                          sectionId = "#n-museums";
                          break;
                        case "Theater":
                        case "Puppentheater":
                          sectionId = "#culture-theatre";
                          break;
                        case "Veranstaltungshalle":
                          sectionId = "#culture-halls";
                          break;
                        case "Galerie":
                          sectionId = "#culture-gallery";
                          break;
                        case "KultureinrichtungSonstiges":
                          sectionId = "#culture-other";
                          break;
                        case "Hallenbad":
                          sectionId = "#indoor-pools";
                          break;
                        case "Freibad":
                          sectionId = "#outdoor-pools";
                          break;
                        case "Tennis":
                          sectionId = "#sports-tennis";
                          break;
                        case "SeilgartenKlettergarten":
                        case "Kletteranlage":
                          sectionId = "#sports-climbing";
                          break;
                        case "Skateanlage":
                          sectionId = "#sports-skating";
                          break;
                        case "Golf":
                          sectionId = "#sports-golf";
                          break;
                        case "StadionArena":
                        case "Fussball":
                          sectionId = "#sports-stadiums";
                          break;
                        case "Eisbahn":
                        case "MountainbikeArena":
                        case "SportSonstiges":
                          sectionId = "#sports-other";
                          break;  
                        case "Sonstiges":
                          sectionId = "#other-events";
                          break;  
                        default:
                          sectionId = null;
                          break;
                      }
              
                      if (sectionId !== null) {
                        let card = document.createElement('div');
                        card.classList.add('card');
              
                        /* let cardImage = document.createElement('div');
                        cardImage.classList.add('card-image');
                        let img = document.createElement('img');
                        img.src = item.image_url;
                        img.alt = "Photo " + item.name;
                        cardImage.appendChild(img);
                        card.appendChild(cardImage); */

                        let cardImage = document.createElement('div');
                        cardImage.classList.add('card-image');
                        let img = document.createElement('img');
                        img.src = item.image_url ? item.image_url : 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/3f/Placeholder_view_vector.svg/681px-Placeholder_view_vector.svg.png';
                        img.alt = "Photo " + item.name;
                        cardImage.appendChild(img);
                        card.appendChild(cardImage);

              
                        let cardHeader = document.createElement('div');
                        cardHeader.classList.add('card-header');
                        let h4 = document.createElement('h4');
                        h4.textContent = item.name;
                        cardHeader.appendChild(h4);
                        card.appendChild(cardHeader);
              
                        let cardBody = document.createElement('div');
                        cardBody.classList.add('card-body');
                        let p = document.createElement('p');
                        p.textContent = "Address: " + item.address;
                        cardBody.appendChild(p);
                        card.appendChild(cardBody);
              
                        let cardFooter = document.createElement('div');
                        cardFooter.classList.add('card-footer');
                        let a = document.createElement('a');
                        a.href = item.link;
                        let button = document.createElement('button');
                        button.textContent = "More Info";
                        a.appendChild(button);
                        cardFooter.appendChild(a);
                        card.appendChild(cardFooter);
                        document.querySelector(sectionId + ' .card-grid').appendChild(card);
                      }
                    });
                  });
              }
              
              get_data();
              
              const nav = document.querySelector('nav');
                const header = document.querySelector('header');

                window.addEventListener('scroll', function() {
                if (window.pageYOffset > header.offsetHeight) {
                    nav.classList.add('fixed');
                } else {
                    nav.classList.remove('fixed');
                }
                });