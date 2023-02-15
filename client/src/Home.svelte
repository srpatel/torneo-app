<script>
  import { link } from "svelte-spa-router";
  import { getContext } from "svelte";

  const contextAction = getContext("torneo-context-action");

  const tournaments = [
    { name: "Triwizard", code: "1" },
    { name: "Duelist Kingdom", code: "2" },
    { name: "There can only be one", code: "3" },
    { name: "Hunger Games", code: "4" },
  ];

  $: if (contextAction)
    $contextAction = {
      href: "/tournament",
      text: "+",
    };
</script>

<ul class="menu bg-base-100 w-56 p-2 rounded-box">
  <li class="menu-title">
    <span>Ongoing tournaments</span>
  </li>
  {#each tournaments as t}
    <li><a href="/tournament/{t.code}" use:link>{t.name}</a></li>
  {/each}
</ul>
