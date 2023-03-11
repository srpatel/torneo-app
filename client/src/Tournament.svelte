<script>
  import { onMount } from "svelte";
  import apiCall from "utils/api-call.js";

  export let params;

  let tournament = null;

  onMount(async () => {
    // Load tournament list from db
    if (params?.code) {
        const response = await apiCall("tournament/" + params.code);
        if (response.isSuccess) {
            tournament = response.data;
        }
    }
  });
</script>

<p>Code: {params?.code}</p>
{#if tournament}
  <p>Name: {tournament.name}</p>
{/if}
