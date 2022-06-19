let card=document.getElementById('card-container');

const projects=[
    {
        title: 'Spring Boot',
        description: 'project made in spring boot 7 crud relations validations and more',
        url:'https://github.com/johngualteros/Project-springboot-disquera'
    },
    {
        title: 'This blog code',
        description: 'project made in django for learn methods of python and java',
        url:'https://github.com/johngualteros/blog-django-python-java'
    },
    {
        title: 'Shop Laravel',
        description: 'Shop made in laravel and materialize it got ORM migrations etc',
        url:'https://github.com/johngualteros/latiendaPHP'
    }
]

const data=()=>{
    projects.map(project=>{
        card.innerHTML+=`
            <div class="card card-body col-md-3 mx-3 bg-info bg-opacity-10 border border-info">
                <div class="card-title text-center text-info fs-2 w-100 fw-bold">${project.title}</div>
                    <p class="text-light fw-bold fs-5">${project.description}</p>
                    <div class="w-100 text-end">
                        <a href="${project.url}" class="text-light fw-bold fs-3" target="_blank"><i class="bi bi-github"></i></a>
                    </div>
            </div>
        `
    })
}
data()