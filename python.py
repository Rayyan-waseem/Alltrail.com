<!DOCTYPE html>
<html lang="en">
<head>
  <title>Alltrail Menu Responsive</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">

<style>

@import url('https://fonts.googleapis.com/css2?family=Raleway:wght@400;500;600&display=swap');

body{
	line-height: 1.5;
	font-family: 'Raleway', sans-serif;
	font-weight: 400;
}
body.hidden-scrolling{
	overflow-y: hidden;
}
*{
	margin:0;
	box-sizing: border-box;
}
.container{
	max-width: 1170px;
	margin:auto;
}
ul{
	list-style: none;
	margin:0;
	padding:0;
}
a{
	text-decoration: none;
}
/header/
.header{
	position: absolute;
	width: 100%;
	left:0;
	top:0;
	z-index: 99;
	padding: 15px;
}
.header-main{
	background-color: #ffffff;
	display: flex;
	align-items: center;
	padding: 10px 0;
	border-radius: 4px;
}
.header .logo{
	padding-right:.01rem;
}

.header .logo a{
	font-size: 30px;
	font-family:cursive;
	color: #2b381f;
	font-weight: 600;
}
.header .logo img{
padding-top:.5rem;
heigth:15%;
width:18%
}
.header .nav-menu{
justify-content:left;
}
.header .menu .menu-item{
	display: inline-block;
	margin-left: 15px;

	position: relative;
}
.header .menu > .menu-item > a{
	display: block;
	padding: 5px 0;
	font-size: 16px;
	font-family:cursive;
	color: #000000;
	text-transform: capitalize;
	font-weight:600;
	transition: all 0.3s ease;
}

.header .menu > .menu-item > a .plus{
	display: inline-block;
	height: 8px;
	width: 8px;
	position: relative;
	margin-left:5px; 
	pointer-events: none;
}
.header .menu > .menu-item > a span{
margin-left:13rem;
}
.header .menu > .menu-item > button{
text-decoration:none;
}

.header .menu > .menu-item > a .plus:before,
.header .menu > .menu-item > a .plus:after{
	content:'';
	position: absolute;
	box-sizing: border-box;
	left: 50%;
	top:50%;
	background-color: #000000;
	height: 2px;
	width: 100%;
	transform: translate(-50%,-50%);
	transition: all 0.3s ease;
}
.header .menu > .menu-item:hover > a .plus:before,
.header .menu > .menu-item:hover > a .plus:after{
   background-color: black;
}
.header .menu > .menu-item > a .plus:after{
   transform: translate(-50%,-50%) rotate(-90deg);	
}
.header .menu > .menu-item > .sub-menu > .menu-item > a:hover,
.header .menu > .menu-item:hover > a{
	color: black;
}
.header .menu > .menu-item > .sub-menu{
	box-shadow: 0 0 10px rgba(0,0,0,0.2);
	width: 220px;
	position: absolute;
	left:0;
	top:100%;
	background-color: #ffffff;
	padding: 10px 0;
	border-radius:15px;
	transform: translateY(10px);
	transition: all 0.3s ease;
	opacity:0;
	visibility: hidden;
}
@media(min-width: 992px){
.header .menu > .menu-item-has-children:hover > .sub-menu{
	transform: translateY(0);
	opacity: 1;
	visibility: visible;
 }
 .header .menu > .menu-item-has-children:hover > a .plus:after{
    transform: translate(-50%,-50%) rotate(0deg);		
 }
}
.header .menu > .menu-item > .sub-menu > .menu-item{
	display: block;
}
.header .menu > .menu-item > .sub-menu > .menu-item > a{
	display: block;
	padding: 10px 20px;
	font-size: 16px;
	font-weight: 600;
	color: #000000;
	transition: all 0.3s ease;
	text-transform: capitalize;
}
.header .open-nav-menu{
	height: 34px;
	width: 40px;
	margin-right: 15px;
	display: none;
	align-items: center;
	justify-content: left;
	cursor: pointer;
}
.header .open-nav-menu span{
	display: block;
	height: 3px;
	width: 24px;
	background-color: #000000;
    position: relative;
}
.header .open-nav-menu span:before,
.header .open-nav-menu span:after{
	content: '';
	position: absolute;
	left:0;
	width: 100%;
	height: 100%;
	background-color: #000000;
	box-sizing: border-box;
}
.header .open-nav-menu span:before{
	top:-7px;
}
.header .open-nav-menu span:after{
	top:7px;
}
.header .close-nav-menu{
	height: 40px;
	width: 40px;
	background-color: #ffffff;
	margin:0 0 15px 15px;
	cursor: pointer;
	display: none;
	align-items: center;
	justify-content: center;
}
.header .close-nav-menu img{
	width: 16px;
}
.header .menu-overlay{
	position: fixed;
	z-index: 999;
	background-color: rgba(0,0,0,0);
	left:0;
	top:0;
	height: 100%;
	width: 100%;
	visibility: hidden;
	opacity:0;
	transition: all 0.3s ease;
}

/home section/
.home-section{
	width: 100%;
	display: block;
	min-height: 100vh;
	background-image: url('../img/home.jpg');
	background-position: center top;
	background-size: cover;
}


/* responsive */

@media(max-width: 991px){
	.header .menu-overlay.active{
	visibility: visible;
	opacity: 1;
}
	.header .nav-menu{
		position: fixed;
		right: -280px;
		visibility: hidden;
		width: 280px;
		height: 100%;
		top:0;
		overflow-y: auto;
		background-color: #222222;
		z-index: 1000;
		padding: 15px 0;
		transition: all 0.5s ease;
	}
	.header .nav-menu.open{
		visibility: visible;
		right: 0px;
	}
	.header .menu > .menu-item{
		display: block;
		margin:0;
	}
	.header .menu > .menu-item-has-children > a{
		display: flex;
		align-items: center;
	}
	.header .menu > .menu-item > a{
		color: #ffffff;
		padding: 12px 15px;
		border-bottom: 1px solid #333333;
	}
	.header .menu > .menu-item:first-child > a{
	    border-top: 1px solid #333333;	
	}

	.header .menu > .menu-item > a .plus:before, 
	.header .menu > .menu-item > a .plus:after{
		background-color: #ffffff;
	}
	.header .menu > .menu-item-has-children.active > a .plus:after{
        transform: translate(-50%,-50%) rotate(0deg);
	}
	.header .menu > .menu-item > .sub-menu{
		width: 100%;
		position: relative;
		opacity: 1;
		visibility: visible;
		border:none;
		background-color: transparent;
		box-shadow: none;
		transform: translateY(0px);
		padding: 0px;
		left: auto;
		top:auto;
		max-height: 0;
		overflow: hidden;
	}
	.header .menu > .menu-item > .sub-menu > .menu-item > a{
		padding: 12px 45px;
		color: #ffffff;
		border-bottom: 1px solid #333333;
	}
	.header .close-nav-menu,
	.header .open-nav-menu{
		display: flex;
	}
}



</style>
</head>
<body>

  <!-- header start -->
  <header class="header">
     <div class="container">
        <div class="header-main">
           <div class="logo">
		   <img src= "logo.png">
              <a href="#">ALLTRAILS </a>
           </div>
           <div class="open-nav-menu">
              <span></span>
           </div>
           <div class="menu-overlay">
           </div>
           <!-- navigation menu start -->
           <nav class="nav-menu">
             <div class="close-nav-menu">
                
             </div>
             <ul class="menu">
                
                <li class="menu-item">
                   <a href="#">Explore</a>
                </li>
                <li class="menu-item">
                   <a href="#">Community</a>
                </li>
				 <li class="menu-item menu-item-has-children">
				
                   <a href="#" data-toggle="sub-menu">Saved<i class="plus"></i></a>
                   <ul class="sub-menu">
                       <li class="menu-item"><a href="#"> My Favourites </a></li>
                       <li class="menu-item"><a href="#"> My Maps </a></li>
                       <li class="menu-item"><a href="#"> Lists </a></li>
                       <li class="menu-item"><a href="#"> Activities </a></li>
					   <li class="menu-item"><a href="#"> Completes </a></li>
					   <li class="menu-item"><a href="#"> Create Map </a></li>
                   </ul>
                </li>
                <li class="menu-item menu-item-has-children">
                   <a href="#" data-toggle="sub-menu">Shop<i class="plus"></i></a>
                   <ul class="sub-menu">
                       <li class="menu-item"><a href="#"> AllTrails Gear </a></li>
                       <li class="menu-item"><a href="#"> Give AllTrails+ </a></li>
					   
                   </ul>
				   <li class="menu-item">
                   <a href="#"><span>Help</span></a>
				 
                </li>
				<li class="menu-item">
                   <button type="submit" class="submit-btn">Log in</button>
				 
                </li>
             </ul>
           </nav>
           <!-- navigation menu end -->
        </div>
     </div>
  </header>
  <!-- header end -->

 <!-- home section start -->
 <section class="home-section">
 </section>
 <!-- home section end -->
 
</body>
</html>
