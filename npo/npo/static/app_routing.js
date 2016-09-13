
app.config(function($urlRouterProvider, $stateProvider, $locationProvider) {

    $urlRouterProvider.otherwise('/404');

	$stateProvider

    .state('start', {
        url: "/",
        templateUrl: '/static/pages/start.htm',
        controller: 'StartPageController',
    })

    .state('nieuwsbrief', {
        url: "/nieuwsbrief",
        templateUrl: '/static/pages/nieuwsbrief.htm',
        controller: 'MagazinePageController',
    })

    .state('lidworden', {
        url: "/lidworden",
        templateUrl: '/static/pages/lidworden.htm',
    })

    .state('overons', {
        url: "/overons",
        templateUrl: '/static/pages/overons.htm',
    })

    .state('beleid', {
        url: "/beleid",
        templateUrl: '/static/pages/beleid.htm',
    })

    .state('natuurgebieden', {
        url: "/natuurgebieden",
        templateUrl: '/static/pages/natuurgebieden.htm',
    })

    .state('soortbescherming', {
        url: "/soortbescherming",
        templateUrl: '/static/pages/soortbescherming.htm',
    })

    .state('activiteiten', {
        url: "/activiteiten",
        templateUrl: '/static/pages/activiteiten.htm',
    })

    .state('404', {
        url: "/404",
        templateUrl: '/static/pages/404.htm',
    })

    ;

    $locationProvider.html5Mode(true);

});
