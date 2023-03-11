<script>
  import apiCall from "utils/api-call.js";
  import { push } from "svelte-spa-router";

  let tournamentName = "";
  let submitting = false;
  let error = null;

  async function handleCreate() {
    submitting = true;
    try {
      const { data, isSuccess } = await apiCall("tournament", {
        name: tournamentName,
        options: {
          type: "elimination",
        },
      });
      if (isSuccess) {
        push("/tournament/" + data.code);
      } else {
        error = data.detail;
      }
    } catch (e) {
      console.error(e);
    }
    submitting = false;
  }
</script>

<div class="form-control w-full max-w-xs">
  {#if error}
    <div class="alert alert-error shadow-lg mb-2">
      <div>
        <span>{error}</span>
      </div>
    </div>
  {/if}
  <input
    type="text"
    placeholder="Tournament name"
    class="input input-bordered w-full max-w-xs mb-2"
    bind:value={tournamentName}
  />
  <button class="btn" on:click={handleCreate} disabled={submitting}
    >Create</button
  >
</div>
