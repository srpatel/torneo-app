<script>
  import Router, { location, link } from "svelte-spa-router";
  import Home from "./Home.svelte";
  import About from "./About.svelte";
  import Number from "./Number.svelte";
  import Link from "./components/Link.svelte";

  let number = 0;

  function randomiseNumber() {
    number = Math.floor(Math.random() * 500);
  }

  randomiseNumber();
</script>

<h1>Torneo</h1>

<nav>
  <Link href="/">Home</Link>
  <Link href="/#/about">About</Link>
  <Link href="/#/number/{number}" on:click={randomiseNumber}>Number</Link>
</nav>

<Router
  routes={{
    "/": Home,
    "/about": About,
    "/number/:number": Number,
  }}
/>
