<script>
  import { link } from "svelte-spa-router";
  import { onMount, getContext } from "svelte";
  import apiCall from "utils/api-call.js";

  const contextAction = getContext("torneo-context-action");

  let tournaments = [];

  $: if (contextAction)
    $contextAction = {
      href: "/tournament",
      text: "+",
    };

  onMount(async () => {
    // Load tournament list from db
    const response = await apiCall("tournament");
    if (response.isSuccess) {
      tournaments = response.data;
    }
  });
</script>

{#if tournaments.length === 0}
  <span class="italic">No tournaments</span>
{:else}
  <ul class="menu bg-base-100 w-56 p-2 rounded-box">
    <li class="menu-title">
      <span>Ongoing tournaments</span>
    </li>
    {#each tournaments as t}
      <li><a href="/tournament/{t.code}" use:link>{t.name}</a></li>
    {/each}
  </ul>
{/if}
